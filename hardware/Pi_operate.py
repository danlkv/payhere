import requests
import RPi.GPIO as GPIO
import time
import bluetooth
import sys
GPIO.setwarnings(False)
hostMACAddress = 'B8:27:EB:CD:AA:98' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
print("Mac address:",hostMACAddress)
port = 3
backlog = 1
size = 1024
#time.sleep.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5) #выствляем в  исходно  положение лепесток
def lookUpNearbyBluetoothDevices():
    print("Scanning...")
    nearby_devices = bluetooth.discover_devices()
    for bdaddr in nearby_devices:
        print( str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")

#lookUpNearbyBluetoothDevices()
print("Starting bluetooth")
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("1")
s.bind(("", port))
print("2")
s.listen(backlog)
print("3")
try:
    client, clientInfo = s.accept()
    print("4")
    while 1:
        data = client.recv(size)
        print("Got data",data)
        if data:
            print(data)
            client.send(data) # Echo back to client
            print(sys.version_info) # запрашиваем версию
            response = requests.POST('url', data=rp)
            html = response.text.decode("utf-8") # utf-8 чтобы принять русские буквы
            if (html==true):
                print("open the door")
                p.ChangeDutyCycle(1.5) #если ответ  с сервера тру то поворачиваем серво на 90  градусов
                time.sleep(1)# ДАТЧик движения не тестил,но впринципе он вроде не сложно работает, его можно прикрутить

    def RCtome(RCpin):    #датчик  движения, который  по идее будет закрывать дверцу ,после того как  единица сменится на ноль в  датчике
        GPIO.setmode(GPIO.BCM)#BCM -pin 16
        GPIO.setup(RCpin,GPIO.IN)
        GPIO.wait_for_edge(RCpin,GPIO.FALLING)
        signal = 1
        while(signal==true):
            signal=GPIO.input(RCpin)
            p.ChangeDuttyCycle(0.5)

    GPIO.cleanup()
except Exception as e: 
    print("erreoe",e)
    print("Closing socket")
    client.close()
s.close()
