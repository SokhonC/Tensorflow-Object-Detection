# -*- coding: utf-8 by Phok Chanrithisak-*-
# -*- Kirirom Institute of Technology-*-
#!/usr/bin/env python
# coding: utf-8

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
from sendEmailAlert.sendEmail import sendEmailAlertFunc
from sendEmailAlert.schedule import *

from .WrapCamera import *

def mainfunc():
    my_main()
    print ('success')