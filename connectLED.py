import requests
from bs4 import BeautifulSoup
import time
import RPi.GPIO as GPIO


webURL ='http://student.crru.ac.th/591463046/keyapi/setroom.php'
r = requests.get(webURL)
r.encoding = 'utf-8'
soup =BeautifulSoup(r.text,'lxml')

LastUpdate = ''
counts = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)


def GoldPriceCheck():
   
        global Name_1,Name_2,Name_3,Name_4,Name_5,Name_6,Name_7,Name_8,Name_9,Status_1,Status_2,Status_3,Status_4,Status_5,Status_6,Status_7,Status_8,Status_9
        Name_1 = soup.find(id = 'name_room_1').text
        Name_2 = soup.find(id = 'name_room_2').text
        Name_3 = soup.find(id = 'name_room_3').text
        Name_4 = soup.find(id = 'name_room_4').text
        Name_5 = soup.find(id = 'name_room_5').text
        Name_6 = soup.find(id = 'name_room_6').text
        Name_7 = soup.find(id = 'name_room_7').text
        Name_8 = soup.find(id = 'name_room_8').text
        Name_9 = soup.find(id = 'name_room_9').text

        
        Status_1 = soup.find(id = 'status_room_1').text
        Status_2 = soup.find(id = 'status_room_2').text
        Status_3 = soup.find(id = 'status_room_3').text
        Status_4 = soup.find(id = 'status_room_4').text
        Status_5 = soup.find(id = 'status_room_5').text
        Status_6 = soup.find(id = 'status_room_6').text
        Status_7 = soup.find(id = 'status_room_7').text
        Status_8 = soup.find(id = 'status_room_8').text
        Status_9 = soup.find(id = 'status_room_9').text
    

while True:

    r = requests.get(webURL)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
   
    GoldPriceCheck()
   
    
    if Status_1 == "1":
        GPIO.output(18,0)
        print ('On :', Name_1)
    else:
        GPIO.output(18,1)
        print ('Off :', Name_1)
        
    if Status_2 == "1":
        GPIO.output(23,0)
        print ('On :', Name_2)
    else:
        GPIO.output(23,1)
        print ('Off :', Name_2)
        
    if Status_3 == "1":
        GPIO.output(24,0)
        print ('On :', Name_3)
    else:
        GPIO.output(24,1)
        print ('Off :', Name_3)
    
    if Status_4 == "1":
        GPIO.output(25,0)
        print ('On :', Name_4)
    else:
        GPIO.output(25,1)
        print ('Off :', Name_4)
        
    if Status_5 == "1":
        GPIO.output(8,0)
        print ('On :', Name_5)
    else:
        GPIO.output(8,1)
        print ('Off :', Name_5)
        
    if Status_6 == "1":
        GPIO.output(7,0)
        print ('On :', Name_6)
    else:
        GPIO.output(7,1)
        print ('Off :', Name_6)
        
    if Status_7 == "1":
        GPIO.output(12,0)
        print ('On :', Name_7)
    else:
        GPIO.output(12,1)
        print ('Off :', Name_7)
        
    if Status_8 == "1":
        GPIO.output(16,0)
        print ('On :', Name_8)
    else:
        GPIO.output(16,1)
        print ('Off :', Name_8)
    
    if Status_9 == "1":
        GPIO.output(20,0)
        print ('On :', Name_9)
    else:
        GPIO.output(20,1)
        print ('Off :', Name_9)


    
    counts = counts+1
    

    # if LastUpdate != lblAsTime:
    #     print(lblAsTime)
    #     print(lblBLSell)
    #     print("00000000000000000000000000000000000000000")
    #     LastUpdate = lblAsTime

    time.sleep(1)
