# -*- coding: utf-8 -*-
import threading
def schedTimeFunc():
    #print('Console Detected:', time.ctime())
    threading.Timer(300, schedTimeFunc).start()

schedTimeFunc()