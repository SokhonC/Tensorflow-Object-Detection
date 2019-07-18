import cv2


class VideoCamera(object):
    def __init__(self):
        # Open a camera
        self.cap = cv2.VideoCapture(0)
        self.is_record = False
        self.out = None
        self.recordingThread = None
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        else:
            return None
