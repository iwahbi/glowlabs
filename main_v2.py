from distutils.log import error
from warnings import catch_warnings
from gpiozero import LED, Button
from time import sleep
import requests;
from alarmSyst import AlarmSys;

AlarmSys=AlarmSys(False)
AlarmSys.show0()

if AlarmSys.ON_OFF.is_pressed:
         AlarmSys.checkstate()
zone1="off"
zone2="off"
zone3="off"
zone4="off"


while True:
    if AlarmSys.status == False and AlarmSys.ON_OFF.is_pressed:
        AlarmSys.count_up()
        AlarmSys.showA()
        AlarmSys.status = True
    elif AlarmSys.status == True and AlarmSys.ON_OFF.is_pressed:
        AlarmSys.cout_down()
        AlarmSys.show0()
        AlarmSys.status = False
    if AlarmSys.status == True:
        if AlarmSys.z1.is_pressed:
            AlarmSys.show1()
            AlarmSys.alarm.blink()
            zone=AlarmSys.checkZone(zone1)
            msg={"z1":zone,"z2":"off","z3":"off","z4":"off"}
            AlarmSys.sendZoneState(msg)
            
            
        elif AlarmSys.z2.is_pressed:
            AlarmSys.show2()
            AlarmSys.alarm.blink()
            zone=AlarmSys.checkZone(zone2)
            msg={"z1":"off","z2":zone,"z3":"off","z4":"off"}
            AlarmSys.sendZoneState(msg)
    
        elif AlarmSys.z3.is_pressed:
            AlarmSys.show3()
            AlarmSys.alarm.blink()
            zone=AlarmSys.checkZone(zone3)
            msg={"z1":"off","z2":"off","z3":zone,"z4":"off"}
            AlarmSys.sendZoneState(msg)
        elif AlarmSys.z4.is_pressed:
           AlarmSys.show4(AlarmSys)
           AlarmSys.alarm.blink()
           zone=AlarmSys.checkZone(zone4)
           msg={"z1":"off","z2":"off","z3":"off","z4":zone}
           AlarmSys.sendZoneState(msg)
        
        elif AlarmSys.reset.is_pressed:
            AlarmSys.alarm.off();
            AlarmSys.resetf()
          
            
    