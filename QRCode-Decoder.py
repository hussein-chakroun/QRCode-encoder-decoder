from pyzbar.pyzbar import decode
from PIL import Image
#enter the path of the qrcode img u want to decode
#change the '\' to '/'
img = Image.open('C:/Users/dread/OneDrive/Desktop/python/myqrcode.png')

result = decode(img)

print(result)