from qr_gen import FileToQR
import display.qr_display as qr_display
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR codes from file")
    parser.add_argument("file_path", help="Path to the file to convert to QR codes")
    args = parser.parse_args()
    
    file_path = args.file_path
    imgobj = FileToQR(file_path).generate_qr()

    qr_display = qr_display.QRDisplay(imgobj)
    qr_display.display()