# Install dependencies
# pip install qrcode
# pip install image

# Import modules
import qrcode
import image

qr = qrcode.QRCode(
  version = 15,
  box_size = 10,
  border = 5
)
data = 'https://www.youtube.com/c/CleverProgrammer'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color= 'white')
img.save('qrcode.png')
