# Create a QR code and display the same

import qrcode

if __name__ == '__main__':
    
    inputText = 'I am Batman'
    
    img = qrcode.make(inputText)
    #print(img,type(img))
    img.show()
    