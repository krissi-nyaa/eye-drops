
from tkinter import Image
import time
import cv2
import argparse

from qreader import QReader
from qr_get.camera import Camera

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read QR codes from camera and save data to file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()
    
    camera = Camera()
    qr_reader = QReader()

    ## Duct tape for now... this stuff needs to be in the right place so i can build it up, but just want functionality fer nao =^_^=

    # For now, let's just assume 60 seconds of data...
    import io
    data = io.BytesIO()
    
    curr_data = b''
    prev_data = b''
    start_time = time.time()
    while time.time() - start_time < 60:
        frame = camera.cam_to_img()
        qr_data = qr_reader.detect_and_decode(frame)
        if qr_data:
            if len(qr_data) > 0:
                if (prev_data != qr_data[0]) and (qr_data[0] != None):
                    ## Now we can encode for some reason??
                    t_data = qr_data[0]
                    if prev_data != t_data:
                        

                        curr_data = qr_data[0]
                        print(f"{curr_data}")
                        data.write(bytes(curr_data.encode('utf-8')))
                        prev_data = curr_data
    data.seek(0)
    # Save the data to a file
    with open(args.output_file, "wb") as f:
        f.write(data.getvalue())