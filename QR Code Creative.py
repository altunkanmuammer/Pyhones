import qrcode
code = qrcode.make('Link')
link = input('Link Giriniz')
code.save('vole1.png')