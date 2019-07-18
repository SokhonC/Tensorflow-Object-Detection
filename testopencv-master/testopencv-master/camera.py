import cv2
#from .utils import label_map_util
#from .utils import visualization_utils as vis_util
class VideoCamera(object):
    def __init__(self):
        # Open a camera
        self.cap = cv2.VideoCapture(0)
        self.cap1 = cv2.VideoCapture('rtsp://zeal:zeal$$$999@10.0.17.10')
        self.is_record = False
        self.out = None
        self.recordingThread = None
    
    def __del__(self):
        self.cap.release()
        self.cap1.release()
    
    def get_frame(self):
        ret, frame = self.cap.read()
    
        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        else:
            return None
    def get_frame1(self):
        ret, frame1 = self.cap1.read()
    
        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame1)
            return jpeg.tobytes()
        else:
            return None