#This is the source code for TIRA (Tactile Interactive Robotic Arm) by V1 Robotics (c)
#This source code is open source and open for any changes
#Windows user may need to install TKinter

from Tkinter import *
import serial

ser = serial.Serial('/dev/tty.usbmodem1411',9600)  #change the serial port accordingly, check in the Arduino IDE


servo1 = 90
servo2 = 90
servo3 = 90
servo4 = 90
servo5 = 90

#servo 1 attributes
#this is for the claw
def servo1_value(servo1_label):
  servo1 = 90
  servo1_label.config(text=str(servo1))

def servo1_up():
    global servo1
    servo1 = 65    #open claw
    servo1_label.config(text=str(servo1))
    ser.write('a')

def servo1_down():
    global servo1
    servo1 = 115    #close claw
    servo1_label.config(text=str(servo1))
    ser.write('s')

def reset_servo1():
    global servo1
    servo1 = 90    #return claw to middle position
    servo1_label.config(text=str(servo1))
    ser.write('d')

#servo 2 attributes
#this is the servo for the limb
def servo2_value(servo2_label):
  servo2 = 90
  servo2_label.config(text=str(servo2))

def servo2_up():
    global servo2
    servo2 = servo2 - 5
    servo2_label.config(text=str(servo2))
    ser.write('f')

def servo2_down():
    global servo2
    servo2 = servo2 + 5
    servo2_label.config(text=str(servo2))
    ser.write('g')

def reset_servo2():
    global servo2
    servo2 = 90
    servo2_label.config(text=str(servo2))
    ser.write('h')

#servo 3 attributes
#this is the servo for the upper limb
def servo3_value(servo3_label):
  servo3 = 90
  servo3_label.config(text=str(servo3))

def servo3_up():
    global servo3
    servo3 = servo3 - 5
    servo3_label.config(text=str(servo3))
    ser.write('j')

def servo3_down():
    global servo3
    servo3 = servo3 + 5
    servo3_label.config(text=str(servo3))
    ser.write('k')

def reset_servo3():
    global servo3
    servo3 = 90
    servo3_label.config(text=str(servo3))
    ser.write('l')


#servo 4 attributes
#this is the servo for the bottom limb
#before assembling the kit, run a python code to make sure both of these two motors are in 90 degrees
#after setting both of the servos in 90 degrees, attach the servo horn to the servo
def servo4_value(servo4_label):
  servo4 = 90
  servo3_label.config(text=str(servo4))

def servo4_up():
    global servo4
    servo4 = servo4 + 3
    servo4_label.config(text=str(servo4))
    ser.write('q')

def servo4_down():
    global servo4
    servo4 = servo4 - 3
    servo4_label.config(text=str(servo4))
    ser.write('w')

def reset_servo4():
    global servo4
    servo4 = 90
    servo4_label.config(text=str(servo4))
    ser.write('e')

#servo 5 attributes
#this is for the servo that makes it turn left and right
def servo5_value(servo5_label):
  servo5 = 90
  servo5_label.config(text=str(servo5))

def servo5_up():
    global servo5
    servo5 = servo5 + 5
    servo5_label.config(text=str(servo5))
    ser.write('r')

def servo5_down():
    global servo5
    servo5 = servo5 - 5
    servo5_label.config(text=str(servo5))
    ser.write('t')

def reset_servo5():
    global servo5
    servo5 = 90
    servo5_label.config(text=str(servo5))
    ser.write('y')


#The below section are for the GUI (Graphical User Interface) variables for controlling TIRA
root = Tk()
root.title("Servo Controller")

title1 = Label(root, text="Servo 1")
title1.grid(row=0, column=0)
servo1_label = Label(root, fg="dark green", font=("Helvetica", 20))
servo1_label.grid(row=1, column=0)
servo1_value(servo1_label)
up1 = Button(root, text='Open', width=10, command=servo1_up)
up1.grid(row=2, column=0)
down1 = Button(root, text='Close', width=10, command=servo1_down)
down1.grid(row=3,column=0)
reset1 = Button(root, text='Reset', command=reset_servo1)
reset1.grid(row=4,column=0)

title2 = Label(root, text="Servo 2")
title2.grid(row=0, column=1)
servo2_label = Label(root, fg="dark green", font=("Helvetica", 20))
servo2_label.grid(row=1, column=1)
servo2_value(servo2_label)
up2 = Button(root, text='Up', width=10, command=servo2_up)
up2.grid(row=2, column=1)
down2 = Button(root, text='Down', width=10, command=servo2_down)
down2.grid(row=3,column=1)
reset2 = Button(root, text='Reset', command=reset_servo2)
reset2.grid(row=4,column=1)

title3 = Label(root, text="Servo 3")
title3.grid(row=0, column=2)
servo3_label = Label(root, fg="dark green", font=("Helvetica", 20))
servo3_label.grid(row=1, column=2)
servo3_value(servo3_label)
up3 = Button(root, text='Up', width=10, command=servo3_up)
up3.grid(row=2, column=2)
down3 = Button(root, text='Down', width=10, command=servo3_down)
down3.grid(row=3,column=2)
reset3 = Button(root, text='Reset', command=reset_servo3)
reset3.grid(row=4,column=2)

title4 = Label(root, text="Servo 4")
title4.grid(row=0, column=3)
servo4_label = Label(root, fg="dark green", font=("Helvetica", 20))
servo4_label.grid(row=1, column=3)
servo4_value(servo4_label)
up4 = Button(root, text='Up', width=10, command=servo4_up)
up4.grid(row=2, column=3)
down4 = Button(root, text='Down', width=10, command=servo4_down)
down4.grid(row=3,column=3)
reset4 = Button(root, text='Reset', command=reset_servo4)
reset4.grid(row=4,column=3)

title5 = Label(root, text="Servo 5")
title5.grid(row=0, column=4)
servo5_label = Label(root, fg="dark green", font=("Helvetica", 20))
servo5_label.grid(row=1, column=4)
servo5_value(servo5_label)
up5 = Button(root, text='Right', width=10, command=servo5_up)
up5.grid(row=2, column=4)
down5 = Button(root, text='Left', width=10, command=servo5_down)
down5.grid(row=3,column=4)
reset5 = Button(root, text='Reset', command=reset_servo5)
reset5.grid(row=4,column=4)

root.mainloop()
