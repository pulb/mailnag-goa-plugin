# mailnag-goa-plugin
Mailnag GNOME Online Accounts plugin.

## Installation

### Ubuntu PPA
This plugin is available in the official [Ubuntu PPA](https://launchpad.net/~pulb/+archive/mailnag).  
Issue the following commands in a terminal to enable the PPA and install the plugin.  

    sudo add-apt-repository ppa:pulb/mailnag
    sudo apt-get update
    sudo apt-get install mailnag-goa-plugin

### Arch Linux
This plugin is available in the official repos.  
Please run `pacman -Syu mailnag-goa-plugin` (as root) to install the package.

### Void Linux
This plugin is available in the official repos.  
Please run `xbps-install -S mailnag-goa-plugin` (as root) in a terminal to install the package.

### Generic Tarballs
Sourcecode releases are available [here](https://github.com/pulb/mailnag-goa-plugin/releases).  
To install the plugin type `sudo ./setup.py install --prefix=/usr --install-layout=deb` in a terminal.
That's it. Now fire up `mailnag-config` and enable the plugin.  

###### Requirements
* mailnag >= 2.0.0
* gir1.2-goa-1.0
* gnome-online-accounts
