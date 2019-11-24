import cv2

cam_urls = ['http://192.168.88.233:8080/video','http://192.168.88.231:8080/video']

caps = [cv2.VideoCapture(cam_url) for cam_url in cam_urls]

while(True):
    for i,cap in enumerate(caps):
        ret, frame = cap.read()
        cv2.imshow(f'frame {i}',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break