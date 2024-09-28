# Practice-Python-8---QR-code-generator-2

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5)
qr.add_data("www.youtube.com/@tevoyager")
qr.make(fit=True)
img = qr.make_image(fill_color="orange",back_color="brown")
img.save("youtube_link.png")
