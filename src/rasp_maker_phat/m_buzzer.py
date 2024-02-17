#! python3

import RPi.GPIO as GPIO
import time


class Buzzer():

    # BCM reference for pin associated with buzzer 
    BUZZER = 26
    
    # on-off status of outputs
    ON  = 1
    OFF = 0


    def __init__(self):
        """ Initialisation
        Warning message      : No
        Reference of pin     : GPIO.BCM
        Pin define as output : one Buzzer
        """
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.BUZZER, GPIO.OUT)

    
    def beep(self, beep_duration = 1.0 ):
        """
        Buzzer beeps for beep_duration seconds
        
        @param beep_duration : number of seconds the buzzer is ON default value = 1.0  second
        @type  beep_duration : integer or float strictly positive
        
        @return : nothing
        """
        GPIO.output(self.BUZZER, self.ON)
        time.sleep(beep_duration)
        GPIO.output(self.BUZZER, self.OFF)

    def beep_repeat( self, number_cycles = 2, beep_duration = 1.0, noiseless_duration = 1.0 ):
        """
        Buzzer beeps number_cycles times, and a cycle starts with a beep.
        The buzzer emits a sound for beep_duration seconds and remains silent for noiseless_duration seconds each cycle.
        
        @param beep_duration   : the duration of a beep and default value = 1.0  second
        @type  beep_duration   : integer or float strictly positive
         
        @param noiseless_duration : number of seconds the buzzer is OFF, and default value = 1.0  second
        @type  noiseless_duration : integer or float strictly positive
        
        @return : nothing
        """        
        for i in range(0, number_cycles):
            self.beep(beep_duration)
            if i < number_cycles:
                time.sleep(noiseless_duration)

#======================================
def main():


   #create the buz obj from the Buzzer class
   buz = Buzzer()
   
   # Buzzer on for one second (default)
   buz.beep()
   time.sleep(1) # Pause before trying another beep
 
   # Buzzer on for 0.2 seconds
   buz.beep(0.2)
   time.sleep(1) # Pause before trying a cycle
   
   # Cyclic operation of the buzzer
   # Cycle: ON for 0.1 seconds and OFF for 0.2 seconds.
   # This cycle is repeated 5 times
   buz.beep_repeat(5, 0.1, 0.2)




if __name__ == "__main__":
    main()
