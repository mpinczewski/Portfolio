import qrcode

img = qrcode.make("http://www.google.pl")
img.save("qr_code\google.jpg")