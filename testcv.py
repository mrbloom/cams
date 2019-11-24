import numpy as np
import cv2
from matplotlib import pyplot as plt

cam_urls = ['http://192.168.88.233:8080/video','http://192.168.88.231:8080/video']

caps = [cv2.VideoCapture(cam_url) for cam_url in cam_urls]

while(True):        
    imgL,imgR = [cap.read()[1] for cap in caps]

    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL,imgR)
    plt.imshow(disparity,'gray')
    plt.show()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break