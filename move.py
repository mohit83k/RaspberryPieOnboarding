from time import sleep

import RPi.GPIO as GPIO

class Move:
	def __init__(self,in1=5,in2=3,in3=31,in4=10,left_pwm_pin=15,right_pwm_pin=13,right_frequency=100,left_frequency=100,duty_cycle=40):
		'''
		Intializing variables:
		
		int1 , in2 , in3 , in4 are 4 GPIO pins used as INPUT to l293d motor driver . 
		left_pwm_pin , right_pwm_pin are pins for Pulse Width Modulation attached to enable pins of l293d motor driver
		'''
		#setting up mode of board
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

		self.in1 = in1
		self.in2 = in2
		self.in3= in3
		self.in4 = in4
		self.left_pwm_pin = left_pwm_pin
		self.right_pwm_pin = right_pwm_pin
		GPIO.setup([in1,in2,in3,in4],GPIO.OUT,initial=False)
		GPIO.setup([self.left_pwm_pin,self.right_pwm_pin],GPIO.OUT,initial=True)
		self.right_frequency = right_frequency
		self.left_frequency = left_frequency
		self.left_pwm = GPIO.PWM(self.left_pwm_pin,self.left_frequency)
		self.right_pwm = GPIO.PWM(self.right_pwm_pin,self.right_frequency)
		self.duty_cycle = duty_cycle

		# Flags
		self.ON = 1
		self.OFF = 0
		self.right_pwm_start = self.OFF
		self.left_pwm_start = self.OFF
		

		




	
	
	def moveBackward(self,timeFrame = -1):
		GPIO.output([self.in2,self.in4],True)
		if timeFrame != -1:
			sleep(timeFrame)
			self.stop()




	def moveForward(self,timeFrame=-1):
		GPIO.output([self.in1,self.in3],True)
		if timeFrame != -1:
			sleep(timeFrame)
			self.stop()
		

	def sharpRight(self,timeFrame=-1):
		GPIO.output(self.in1,True)
		if timeFrame != -1:
			sleep(timeFrame)
			self.stop()

	def sharpLeft(self,timeFrame=-1):
		GPIO.output(self.in3,True)
		if timeFrame != -1:
			sleep(timeFrame)
			self.stop()
		
	def swiftForwardRight(self,timeFrame = -1):
		self.moveForward()
		self.right_pwm.start(self.duty_cycle)
		self.right_pwm_start = self.ON
		if timeFrame != -1:
			sleep(timeFrame)
			stop()


	def swiftForwardLeft(self,timeFrame = -1):
		self.moveForward()
		self.left_pwm.start(self.duty_cycle)
		self.left_pwm_start = self.ON
		if timeFrame !=-1:
			sleep(timeFrame)
			self.stop()

	def swiftBackwardRight(self,timeFrame = -1):
		self.moveBackward()
		self.right_pwm.start(self.duty_cycle)
		self.right_pwm_start = self.ON
		if timeFrame !=-1:
			sleep(timeFrame)
			self.stop()


	def swiftBackwardLeft(self,timeFrame = -1):
		self.moveBackward()
		self.left_pwm.start(self.duty_cycle)
		self.left_pwm_start = self.ON
		if timeFrame !=-1:
			sleep(timeFrame)
			self.stop()



	def stop(self):
		#stop logic
		GPIO.output([self.in1,self.in2,self.in3,self.in4],False)
		if (self.right_pwm_start):
			#self.right_pwm.stop()
			#GPIO.output(self.right_pwm_pin,True)
                        self.right_pwm.ChangeDutyCycle(100)

			self.right_pwm_start = self.OFF
		if (self.left_pwm_start):
			#self.left_pwm.stop()
			#GPIO.output(self.left_pwm_pin,)
			self.right_pwm.ChangeDutyCycle(100)
			print "left pwm 100"
			self.left_pwm_start = self.OFF



obj = Move()

while(True):
	ch = raw_input("Enter text: ")
	if ch == 's':
		obj.stop()
	elif ch == 'w':
		obj.moveForward()
	elif ch == 'x':
		obj.moveBackward()
	elif ch == 'a':
		obj.sharpLeft()
	elif ch == 'd':
		obj.sharpRight()
	elif ch == 'e':
		obj.swiftForwardRight()
	elif ch == 'q':
                obj.swiftForwardLeft()
    elif ch == 'z':
                obj.swiftBackwardLeft()
    elif ch == 'c':
                obj.swiftBackwardLeft()
            
	else:
        obj.stop()
		exit()







	
		