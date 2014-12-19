#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# goaplugin.py
#
# Copyright 2014 Patrick Ulbrich <zulu99@gmx.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#

from gi.repository import Goa
from Mailnag.common.plugins import Plugin, HookTypes
from Mailnag.common.accounts import Account
from Mailnag.common.i18n import _

plugin_defaults = {}


class GOAPlugin(Plugin):
	def __init__(self):
		self._accounts_loaded_hook = None

	
	def enable(self):
		def accounts_loaded_hook(accounts):
			client = Goa.Client.new_sync(None)
			goa_accounts = client.get_accounts()
			
			for a in goa_accounts:
				mail = a.get_mail() # get the mail interface
				
				if (mail != None) and (not a.get_account().props.mail_disabled):
					if mail.props.imap_supported:
						passwd = ''
						auth_string = ''
						
						pwd_based = a.get_password_based()
						if pwd_based != None:
							passwd = pwd_based.call_get_password_sync('imap-password', None)
						else:
							oauth2_based = a.get_oauth2_based()
							if oauth2_based != None:
								token = oauth2_based.call_get_access_token_sync(None)
								# TODO: this authstring is probably GMail specific
								# (Check a.get_account().props.provider_name == 'Google' ?)
								# See : http://google-mail-oauth2-tools.googlecode.com/svn/trunk/python/oauth2.py
								auth_string = 'user=%s\1auth=Bearer %s\1\1' % (mail.props.imap_user_name, token[0])
							
						# Append GOA account to Mailnag accounts (if any)
						if (passwd != '') or (auth_string != ''):
							acc = Account(enabled = True, name = mail.props.email_address, \
									user = mail.props.imap_user_name, password = passwd, \
									oauth2string = auth_string, server = mail.props.imap_host, port = '', \
									ssl = mail.props.imap_use_ssl, imap = True, idle = True, folder = '')
							
							accounts.append(acc)
		
		
		self._accounts_loaded_hook = accounts_loaded_hook
		
		controller = self.get_mailnag_controller()
		hooks = controller.get_hooks()
		
		hooks.register_hook_func(HookTypes.ACCOUNTS_LOADED, 
			self._accounts_loaded_hook)
		
	
	def disable(self):
		controller = self.get_mailnag_controller()
		hooks = controller.get_hooks()
		
		if self._accounts_loaded_hook != None:
			hooks.unregister_hook_func(HookTypes.ACCOUNTS_LOADED,
				self._accounts_loaded_hook)
			self._accounts_loaded_hook = None

	
	def get_manifest(self):
		return (_("GNOME Online Accounts"),
				_("GNOME Online Accounts Integration."),
				"1.0",
				"Patrick Ulbrich <zulu99@gmx.net>",
				False)


	def get_default_config(self):
		return plugin_defaults
	
	
	def has_config_ui(self):
		return False
	
	
	def get_config_ui(self):
		return None
	
	
	def load_ui_from_config(self, config_ui):
		pass
	
	
	def save_ui_to_config(self, config_ui):
		pass
