# Указываем инфу о пакете
pkgname=bonchcli
pkgver=0.0.4
pkgrel=1
pkgdesc="CLI client of lk.sut.ur"
arch=('any')
url="https://github.com/karimullinarthur/bonchcli"
license=('MIT')
depends=('python', 'python-poetry')  # Указываем зависимости

# Источник — архив с гитхаба (замени ссылку на свою)
source=("$pkgname-$pkgver.tar.gz::https://github.com/твой-гит/myapp/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')  # Можно заменить на реальный хеш, посчитав командой `sha256sum файл`

build() {
    cd "$pkgname-$pkgver"
    poetry build  # Собираем wheel-архив
}

package() {
    cd "$pkgname-$pkgver"
    poetry install --root="$pkgdir" --no-dev  # Устанавливаем в pkgdir без dev-зависимостей
}

