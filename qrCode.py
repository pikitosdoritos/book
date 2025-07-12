import pyqrcode
import png
from pyqrcode import QRCode

# 1 variant
url = pyqrcode.create('https://github.com/pikitosdoritos')

url.svg('myqr.svg', scale = 8)
url.png('myqr.png', scale = 6)

# 2 variant
s = 'https://github.com/pikitosdoritos'

url = pyqrcode.create(s)

url.svg('myqr.svg' scale = 8)
url.png('myqr.png', scale = 6)