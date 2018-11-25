
from picamera import PiCamera
from time import sleep

def main():
    camera = PiCamera()
    camera.start_preview()
    while True:
        sleep(2)
        print("capture")
        camera.capture('/home/pi/payhere/camera/test.jpg')
    camera.stop_preview()

if __name__=="__main__":
    main()
