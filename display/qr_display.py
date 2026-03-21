from PIL import ImageShow, Image

class QRDisplay:
    def __init__(self, imgobj):
        self.imgobj = imgobj

    def display(self):
        with Image.open(self.imgobj, formats=["GIF"]) as img:
            viewer = ImageShow.WindowsViewer() # ew.. but ya, home computer...
            viewer.format = "GIF"
            viewer.show(image=img, format="GIF")