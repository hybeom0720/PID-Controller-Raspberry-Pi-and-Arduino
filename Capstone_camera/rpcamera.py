from picamera import PiCamera
from time import sleep



def camera_capture: 
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Desktop/server/image.jpg')
    camera.stop_preview()

#if문으로 버튼 눌렀을 때 비디오 저장되는거 만들기
def video_capture(self, capture_time = 5)
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/server/video.h264')
    sleep(capture_time)
    camera.stop_recording()
    camera.stop_preview()