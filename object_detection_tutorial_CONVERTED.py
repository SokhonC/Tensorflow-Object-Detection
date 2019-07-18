import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import threading
import time
import cv2
from utils import label_map_util
from utils import visualization_utils as vis_util
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
    
    
    
    
sys.path.append("..")
MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')
NUM_CLASSES = 90
    
    
detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
  serialized_graph = fid.read()
  od_graph_def.ParseFromString(serialized_graph)
  tf.import_graph_def(od_graph_def, name='')
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)
       
    #calling class from other file
    
def load_image_into_numpy_array(image):
      (im_width, im_height) = image.size
      return np.array(image.getdata()).reshape(
          (im_height, im_width, 3)).astype(np.uint8)
#PATH_TO_TEST_IMAGES_DIR = 'test_images'
#TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 3) ]
#IMAGE_SIZE = (12, 8)
cap1 = cv2.VideoCapture(0)
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
    while 1:
      ret1,frame1 = cap1.read()
      frame1_expanded = np.expand_dims(frame1, axis=0)
      image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
      boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
      scores = detection_graph.get_tensor_by_name('detection_scores:0')
      classes = detection_graph.get_tensor_by_name('detection_classes:0')
      num_detections = detection_graph.get_tensor_by_name('num_detections:0') 
      (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: frame1_expanded})
      vis_util.visualize_boxes_and_labels_on_image_array(
          frame1,
          np.squeeze(boxes),
          np.squeeze(classes).astype(np.int32),
          np.squeeze(scores),
          category_index,
          use_normalized_coordinates=True,
          line_thickness=8)
      cv2.imshow('Camera 1',cv2.resize(frame1,(800,600)))
      console_print = False
      min_score_thresh = 0.5
      print([category_index.get(i) for i in classes[0]])
      print(boxes.shape)
      print(num_detections)
      #print([category.get(1)] for i in classes[0] if scores[0, i] > min_score_thresh)
      if cv2.waitKey(25) & 0xFF == ord('s'):
          break
          cv2.destroyAllWindows()
          cap1.release()
