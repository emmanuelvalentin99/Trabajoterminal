"""import time
from base_camera import BaseCamera


class Camera(BaseCamera):
    An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second.
    imgs = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 3]
"""

import cv2
from base_camera import BaseCamera

class Camera(BaseCamera):
    
    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter('./static/video.avi',fourcc, 20.0, (640,480))
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            out.write(img)
            # encode as a png image and return it
            yield cv2.imencode('.png', img)[1].tobytes()
        out.release()       
    '''
    def init_record():
        camera = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter('./static/video.avi',fourcc, 20.0, (640,480))
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            out.write(img)
            # encode as a png image and return it
            yield cv2.imencode('.png', img)[1].tobytes()
        out.release()
    '''