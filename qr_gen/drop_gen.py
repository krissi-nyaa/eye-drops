import io
import qrcode
import logging
import base64
from .qr_buff import QRBuff

logging.basicConfig(level=logging.INFO)


class FileToQR:
    def __init__(self, file_path):
        self.file_path = file_path
        self.card_count = 0
        
        self.imgobj = io.BytesIO()
        

    def generate_qr(self):
    
        with open(self.file_path, 'rb') as file:
            data = file.read()
        ## Break up data into 2950 byte chunks
        # Base64 gives us a 33% overhead xD ... gotta big brain a better fix for this
        chunks = [base64.b64encode(data[i:i+1500]) for i in range(0, len(data), 1500)]
        
        qr_buff = QRBuff()
        for chunk in chunks:
            t_qr = qrcode.QRCode(version=40)
            t_qr.add_data(chunk)
            qr_buff.push(
                t_qr.make_image(fill_color="black", back_color="white")
            )
            self.card_count += 1
            logging.info(f"Generated QR card {self.card_count} with {len(chunk)} bytes of data.")

        qr_buff.cards[0].save(self.imgobj, format="GIF", append_images=qr_buff.cards[1:], duration=2000)
        self.imgobj.seek(0)
        return self.imgobj