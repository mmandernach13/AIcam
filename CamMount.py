from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import time 

class CamMount:
    def __init__(self, pan_servo_pin=18, tilt_servo_pin=19): # default connects to GPIO18 and GPIO19
        
        factory = PiGPIOFactory()   # configure for hardware PWM (more precise)
        
        # servos can rotate 120deg +/- 10deg
        # to be safe, limit rotation to 110deg w 0 as the midpoint
        self.pan_servo = AngularServo(pan_servo_pin, min_angle=-55, max_angle=55, pin_factory=factory)
        self.tilt_servo = AngularServo(tilt_servo_pin, min_angle=-55, max_angle=55, pin_factory=factory)

        self.pan_servo.mid()
        self.tilt_servo.mid()

        self.ppos = 0
        self.tpos = 0

    def update(self):
        self.pan_servo.angle = self.ppos
        self.tilt_servo.angle = self.tpos

    def set_pos(self, ppos=0.0, tpos=0.0):
        
        if ppos < -55:
            ppos = -55
        if ppos > 55:
            ppos = 55
        if tpos < -55:
            tpos = -55
        if tpos > 55:
            tpos = 55

        self.ppos = ppos 
        self.tpos = tpos 

        self.update()

    def pan(self, deg=0.0, direction='left'):
        
        if direction == 'left':
            tmp = self.ppos + deg 
        elif direction == 'right':
            tmp = self.ppos - deg

        if tmp < -55:
            tmp = -55
        elif tmp > 55:
            tmp = 55

        self.ppos = tmp
        
        self.update()

    def tilt(self, deg=0.0, direction='up'):
        
        if direction == 'up':
            tmp = self.tpos + deg
        elif direction == 'down':
            tmp = self.tpos - deg 

        if tmp < -55:
            tmp = -55
        elif tmp > 55:
            tmp = 55

        self.tpos = tmp
        self.update()

    def disconnect(self):
        
        self.set_pos()
        time.sleep(0.5)
        self.pan_servo.detach()
        self.tilt_servo.detach()



if __name__ == "__main__":
    mount = CamMount()

    tilt_step = 1
    pan_step = 1

    tilt_dir = 'up'
    pan_dir = 'right'

    try:
        while True:
            mount.tilt(tilt_step, tilt_dir)
            mount.pan(pan_step, pan_dir)
        
            
            time.sleep(0.05)
    except KeyboardInterrupt:
        mount.disconnect()
        print("\ndetatched successfully")



