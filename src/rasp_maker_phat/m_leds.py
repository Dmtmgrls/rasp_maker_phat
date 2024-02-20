#! python3

import RPi.GPIO as GPIO
import time


class Leds():

    # BCM reference for pins associated with Leds 
    LED_0 = 17
    LED_1 = 18
    LED_2 = 27
    LED_3 = 22
    LED_4 = 25
    LED_5 = 12
    LED_6 = 13
    LED_7 = 19
    LED = [LED_7, LED_6, LED_5, LED_4, LED_3, LED_2, LED_1, LED_0]


    # on-off status of outputs
    ON = 1
    OFF = 0


    def __init__(self):
        """ Initialisation
        Warning message    : No
        Reference of pin      : GPIO.BCM
        Pin define as output : 8 LED and one Buzzer
        Pin define as input   : Switch
        """
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)

        for i in range(0,len(self.LED)):
            GPIO.setup(self.LED[ i ], GPIO.OUT)

    # Destructor
    def __del__(self):
        # only affects the LED pins, and no other GPIO pins
        GPIO.cleanup(self.LED)
    
    # GETTER
    def led_range( self ):
        return range(0,8)
    
    # METHODES
    def flash( self, led_n , tempo = 1.0 ):
        """
        Set ON the Led number <led_n> for <tempo> seconds
        
        @param led_n   : must be in range(0,8)
                                  0 corresponds to the rightmost Led of Maker pHat
                                  7 to the leftmost Led
        @type led_n      : integer
        
        @param tempo : number of seconds the Led is ON  
                                  default value = 1.0  second
        @type tempo    : integer or float strictly positive
        
        @return : nothing
        """
        led_pin = self.LED[led_n]
        GPIO.output( led_pin , self.ON )
        time.sleep(tempo)
        GPIO.output( led_pin , self.OFF )
            

    def flash_mask( self, mask, tempo = 1.0 ):
        """
        Switch ON all Leds whose <mask> bits are set to 1 for <tempo> seconds

        @param mask   : must be from 0x01 to 0xFF
                                  0x01 corresponds to the rightmost Led of Maker pHat
                                  0x80 to the leftmost Led
                                  Warnning : if mask = 0x00 then all Led are not will not be modified
        @type mask    : integer
        
        @param tempo  : number of seconds the Led is ON  default value = 1.0  second
        @type  tempo  : integer or float strictly positive
        
        @return       : nothing
        """        
        prob = 0x01
        led_on = []

        #Selected Led set ON 
        for led_n in range(0,8):
            if prob & mask != 0 :
                GPIO.output(self.LED[ led_n ] , self.ON)
                led_on.append( led_n )
            prob = prob<<1
        
        time.sleep(tempo)

        # Selected Led se OFF
        for led_n in led_on:
            GPIO.output(self.LED[ led_n ], self.OFF)

 
    def set_on_leds( self, mask = 0x00):
        """
        Set ON all Leds whose <mask> bits are set to 1

        @param mask   : must be from 0x01 to 0xFF
                                  0x01 corresponds to the rightmost Led of Maker pHat
                                  0x80 to the leftmost Led
                                  Warnning : if mask = 0x00 then all Led are not will not be modified
        @type mask    : integer
        
        @return       : nothing
        """ 
        prob = 0x01      
        for led_n in range(0,8):
            if prob & mask != 0:
                GPIO.output(self.LED[ led_n ] , self.ON)
            prob = prob<<1

    def set_off_leds( self, mask = 0x00):
        """
        Set OFF all Leds whose <mask> bits are set to 1

        @param mask   : must be from 0x01 to 0xFF
                                  0x01 corresponds to the rightmost Led of Maker pHat
                                  0x80 to the leftmost Led
                                  Warnning : if mask = 0x00 then all Led are not will not be modified
        @type mask    : integer
        
        @return       : nothing
        """         
        prob = 0x01      
        for led_n in range(0,8):
            if prob & mask != 0:
                GPIO.output(self.LED[ led_n ] , self.OFF)
            prob = prob<<1              

    def cleanup(self):
        # only affects the LED pins, and no other GPIO pins
        GPIO.cleanup(self.LED)
    
#======================================
def main():
    import time

    leds = Leds()

    for i in leds.led_range():
        leds.flash( i, 0.2 )
        
    for i in [6,5,4,3,2,1,0]:
        leds.flash( i, 0.2 )

  
    leds.set_off_leds( 0xFF)
    leds.flash_mask( 0x33 )
    leds.flash_mask( 0xCC )
    leds.flash_mask( 0xF0 )
    leds.flash_mask( 0x0F )

    leds.set_off_leds( 0xFF)
    tempo =  0.6
    leds.flash_mask( 0xAA , tempo)
    leds.flash_mask( 0x55 , tempo)
    leds.flash_mask( 0xF0 , tempo)
    leds.flash_mask( 0x0F , tempo)

    del leds
    
if __name__ == "__main__":
    main()
