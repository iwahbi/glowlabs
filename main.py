from gpiozero import LED, Button
from time import sleep
from alarmSyst import AlarmSys;

AlarmSys=AlarmSys(False)
AlarmSys.show0()

if AlarmSys.ON_OFF.is_pressed:
         AlarmSys.checkstate()

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
            AlarmSys.alarm.on()

        elif AlarmSys.z2.is_pressed:
            AlarmSys.show2()
            AlarmSys.alarm.on()
        elif AlarmSys.z3.is_pressed:
            AlarmSys.show3()
            AlarmSys.alarm.on()
        elif AlarmSys.z4.is_pressed:
           AlarmSys.show4(AlarmSys)
           AlarmSys.alarm.on()
        elif AlarmSys.reset.is_pressed:
            AlarmSys.resetf()