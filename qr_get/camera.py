import cv2 as cv
import io
 
class Camera:
    def __init__(self):
        self.cap = cv.VideoCapture(0)
        self.blob = io.BytesIO()
        if not self.cap.isOpened():
            print("Gunna need new cams...")
            exit()
    
    def cam_to_img(self):
        ret, frame = self.cap.read()
        if not ret:
            print("cam ded lols get rekt...")
            return None
        # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imwrite(self.blob, frame)
        self.blob.seek(0)
        return frame

    
    # fer debuggen
    def _display_frame(self, frame):
        cv.imshow('frame', frame)
        while True:
            if cv.waitKey(1) == ord('q'):
                break
        return True

    def release(self):
        self.cap.release()
        cv.destroyAllWindows()
