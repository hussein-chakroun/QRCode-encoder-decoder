import qrcode

#Enter prefered text or link to be displayed when scanning the qrcode
data = "https://brilliant-creponne-c39b1c.netlify.app/" 

qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

#Choose the qrcode color and backgrount color
img = qr.make_image(fill_color = 'Black', back_color = 'white')

#Enter the path where u want the qrcode image to be stored in
img.save('C:/Users/dread/OneDrive/Desktop/python/myqrcode.png')