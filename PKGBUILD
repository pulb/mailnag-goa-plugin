# Maintainer: Patrick Ulbrich <zulu99 at gmx . net>

pkgname=mailnag-goa-plugin
pkgver=1.1.0
pkgrel=1
pkgdesc="Mailnag GNOME Online Accounts Plugin"
arch=('any')
url="https://github.com/pulb/mailnag-goa-plugin"
license=('GPL')
depends=('mailnag' 'gnome-online-accounts')
source=('https://github.com/pulb/mailnag-goa-plugin/archive/v1.1.0.tar.gz')
md5sums=('f3c0df790a2f5e6b615ef804ee0e5a91')

package() {
  cd $pkgname-$pkgver
  python2 setup.py install --root="$pkgdir"
}
