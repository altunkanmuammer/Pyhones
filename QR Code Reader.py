from pyzbar import pyzbar
from Pıl import image
qr = pyzbar.decode{image.open{"vol1.png"}}
print{qr{0}.data.decode{"ascii"}}