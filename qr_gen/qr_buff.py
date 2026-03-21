import qrcode
from PIL import Image

class QRBuff:
    def __init__(self):
        self.cards = []

    def pop(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            return None
        
    def push(self, data):
        self.cards.append(data)

# img = qrcode.make('Some data here')

# img2 = qrcode.make('woofwoofwoof')

# images = [img, img2]

# images[0].save('qr1.gif', append_images=images[1:],duration=500, loop=0)

