#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import RPi.GPIO as GPIO
import time
import bluetooth
import sys
import json
hostMACAddress = 'B8:27:EB:CD:AA:98' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
ipAdress='https://Lykov.tech'

def lookUpNearbyBluetoothDevices():
    print("Scanning...")
    nearby_devices = bluetooth.discover_devices()
    for bdaddr in nearby_devices:
        print( str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")
        
def verifyTx(txHash,client_key):
    return True
    ver=requests.get(FantomApi+txHash)
    ver=json.loads(ver.text)
    print("FantomTx(from server)",ver['from'])
    print("CLient key",client_key)
    if ver['from']==client_key:
        return True

def beep(ps,dur=0.2):
    print('beep')
    ps.ChangeDutyCycle(50)
    time.sleep(0.2)
    ps.ChangeDutyCycle(0.0)

def main():
    #lookUpNearbyBluetoothDevices()
    PaymentEventApi = 'http://lykov.tech:3030/payEvent'

    GPIO.setwarnings(False)
    print("Mac address:",hostMACAddress)
    port = 3
    backlog = 1
    size = 1024
    #time.sleep.setmode(GPIO.BOARD)
    GPIO.setmode(GPIO.BCM)
    pin =7
    pin_sound = 4
    GPIO.setup(pin,GPIO.OUT)
    GPIO.setup(pin_sound,GPIO.OUT)
    MY_ADRESS='0x01';
    p = GPIO.PWM(pin,50)
    ps= GPIO.PWM(pin_sound,1000)
    p.start(12.5) #выствляем в  исходно  положение лепесток
    ps.start(0.0)

    beep(ps,dur=0.1)
    time.sleep(0.1)
    beep(ps,dur=0.2)
    while 1:
        data=requests.get(PaymentEventApi)
        rp=json.loads(data.text)
        #rp = {}
        txHash = rp.get('txHash')
        client_key = rp.get('client_addr')
        print("hash and key:",txHash,client_key)
        ifOpen=verifyTx(txHash,client_key)
        if (ifOpen==True):

            beep(ps,dur=0.4)
            time.sleep(0.2)
            beep(ps,dur=0.1)
            time.sleep(0.1)
            beep(ps,dur=0.1)
            print("open the door")
            p.ChangeDutyCycle(7.5) #если ответ  с сервера тру то поворачиваем серво на 90  градусов
            time.sleep(2)

            # CLOSE
            beep(ps,dur=0.1)
            print("close the door")
            p.ChangeDutyCycle(12.5)
            time.sleep(3)

    def RCtome(RCpin):    #датчик  движения, который  по идее будет закрывать дверцу ,после того как  единица сменится на ноль в  датчике
        GPIO.setmode(GPIO.BCM)#BCM -pin 16
        GPIO.setup(RCpin,GPIO.IN)# ДАТЧик движения не тестил,но впринципе он вроде не сложно работает, его можно прикрутить
        GPIO.wait_for_edge(RCpin,GPIO.FALLING)
        signal = 1
        while(signal==True):
            signal=GPIO.input(RCpin)
            p.ChangeDuttyCycle(0.5)
    GPIO.cleanup()
if (__name__=="__main__"):
    try:
        main()
    except Exception as e: 
        print("erreoe",e)
