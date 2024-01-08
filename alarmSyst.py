#from select import select
#from telnetlib import STATUS
#from tkinter import Button

from operator import ne
import string
from gpiozero import LED, Button
from time import sleep
import requests;
class AlarmSys:
    z1:Button
    z2:Button
    z3:Button
    z4:Button
    ON_OFF:Button
    reset : Button
    a:LED
    b:LED
    c:LED
    d:LED
    e:LED
    f:LED
    g:LED
    alarm : LED
    status : bool

    #another constructor
    def __init__ ( self,status:bool) :

        self.status= status
        self.a = LED(8)
        self.b = LED(9)
        self.c = LED(10)
        self.d = LED(11)
        self.e = LED(12)
        self.f = LED(13)
        self.g = LED(17)
        #self.alarm=LED(19)  #this gpio is z4's i will have to change it to GPIO21(21)
        self.alarm=LED(21) 

        self.ON_OFF = Button(27)
        #####################
             ###########################################
            #Alarm zones
        self.z1 = Button(22)
        self.z2 = Button(5)
        self.z3 = Button(6)
        self.z4 = Button(19)
       # self.z4 = Button(19) #i lent the gpio to the Led alarm
        self.reset=Button(2)#put gpio
            #False= unarmed, True= armed

    def resetf(self) :
            self.showA()
            self.alarm.off()
    def checkstate(self) :
        if self.__status==True:
            status=False
            self.alarm.off()
            self.cout_down()
        else:
            status=True  
            self.count_up()
    def show0(self):
    #0
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.off()
        self.e.off()
        self.f.off()
        self.g.on()
    def show1(self):
    #1
        self.a.on()
        self.b.off()
        self.c.off()
        self.d.on()
        self.e.on()
        self.f.on()
        self.g.on()
    def show2(self):
            #2
        self.a.off()
        self.b.off()
        self.c.on()
        self.d.off()
        self.e.off()
        self.f.on()
        self.g.off()
    def show3(self):
        #3
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.off()
        self.e.on()
        self.f.on()
        self.g.off()
    def show4(self):
        #4
        self.a.on()
        self.b.off()
        self.c.off()
        self.d.on()
        self.e.on()
        self.f.off()
        self.g.off()
    def show5(self):
        #5
        self.a.off()
        self.b.on()
        self.c.off()
        self.d.off()
        self.e.on()
        self.f.off()
        self.g.off()
    def show6(self):
            #6
        self.a.off()
        self.b.on()
        self.c.off()
        self.d.off()
        self.e.off()
        self.f.off()
        self.g.off()
    def show7(self):
        #7
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.on()
        self.e.on()
        self.f.on()
        self.g.on()
    def show8(self):
        #8
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.off()
        self.e.off()
        self.f.off()
        self.g.off()
    def show9(self):
        #9
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.off()
        self.e.on()
        self.f.off()
        self.g.off()
    def showA(self):
            #A
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.on()
        self.e.off()
        
        self.f.off()
        self.g.off()
    def count_up(self):
        #0
        self.show0()
        sleep(1)
        #1
        self.show1()
        sleep(1)
        #2
        self.show2()
        sleep(1)
        #3
        self.show3()
        sleep(1)
        #4
        self.show4()
        sleep(1)
        #5
        self.show5()
        sleep(1)
        #6
        self.show6()
        sleep(1)
        #7
        self.show7()
        sleep(1)
        #8
        self.show8()
        sleep(1)
        #9
        self.show9()
        sleep(1)
    def cout_down(self):
        
        
            #9
        self.show9()
        sleep(1)
        #8
        self.show8()
        sleep(1)
        #7
        self.show7()
        sleep(1)
        #6
        self.show6()
        sleep(1)
        #5
        self.show5()
        sleep(1)
        #4
        self.show4()
        sleep(1)
        #3
        self.show3()
        sleep(1)
        #2
        self.show2()
        sleep(1)
        #1
        self.show1()
        sleep(1)
        #0
        self.show0()
        sleep(1)
    def checkZone(self,zonestate:string):
            if zonestate=="off":
                    zonestate="on"               
            else:
                zonestate="off"
            newzone=zonestate
            return newzone
    def sendZoneState(self,msg:string):          
            try :
                msgrequest=requests.get("https://alarmsystempoclab3.000webhostapp.com/",params=msg)
                #msgrequest=requests.get("http://192.168.1.121:8081/secuServeur.php",params=msg)
                #msgrequest=requests.get("http://192.168.2.19:61842/UpdatePiZones.aspx",params=msg)
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                raise SystemExit(e)
            
            