from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

#if문으로 버튼 눌렀을 떄 실행되는거 만들기
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/programs/photo/image.jpg')
camera.stop_preview()

#if문으로 버튼 눌렀을 때 비디오 저장되는거 만들기
camera.start_preview()
camera.start_recording('/home/pi/Desktop/programs/photo/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()