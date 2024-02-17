#! python3

import RPi.GPIO as GPIO
import time
import sys
import traceback


class Buttons():
    """ Manages the three push buttons (switchs) of the maker-pHAT card """


    # Structured information
    T_SWITCH_NAME  = ("sw1", "sw2", "sw3") 
    T_SET_CODE_PIN = (21, 16, 20)
    DICO_SWITCH_NAME_TO_PIN_CODE = { "sw1" : 21, "sw2" : 16, "sw3" : 20 }
    DICO_PIN_CODE_TO_SWITCH_NAME = { 21 : "sw1", 16 : "sw2", 20 : "sw3" }

    # on-off status of outputs
    ON  = 0
    OFF = 1


    def __init__(self):
        """ 
        Warning message       : No
        Pin reference mode    : GPIO.BCM

        Remark : the initialization of the three pins assigned to the 3 push buttons will be carried out
                     by the /add_event_detect_switch/ method.
                 This methode avoids any pin programming errors when using the Buttons class.
        """

        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)

   
    def title( size, my_title ):
        # This function is internal to the class. It is only used for error messages.  
        # Displays a line of format ====== my_title ======
        #  -  size     : is the number of "=" characters which surrounds my_title.
        #                the number of characters "=" is the same on the left as on the right
        #  -  my_title : is the title you want to display between the characters "===="
        print( "\n" + "="*size + my_title + "="*size + "\n" )
                
 
    def empty(gpio_pin_code):
        """ 
        Default internal callback function that does nothing
        User-defined callback functions should only have one input parameter.
        This parameter represents the GPIO.BCM reference of the pin associated with the push button.
        The name of this parameter 'gpio_pin_code' is very self-explanatory
        """
        pass


    @property
    def list_of_switch_pins(self):
        """ return the list of BCM references of the 3 pins associated with the 3 witchs of the Maker_pHAT card """
        return self.T_SET_CODE_PIN   


    @property
    def list_of_switch_names(self):
        """ return list of switch names which are screen printed on the maker-pHAT card """
        return self.T_SWITCH_NAME    


    @property
    def dico_switch_name_to_pin_code(self):
        """ return the dictionary of couples (switch_name, pin_code) where switch_name is the key """
        return self.DICO_SWITCH_NAME_TO_PIN_CODE


    @property
    def dico_pin_code_to_switch_name(self):
        """ return the dictionary of couples (pin_code, switch_name) where code_pin is the key """
        return self.DICO_PIN_CODE_TO_SWITCH_NAME



    #=========================================
    # Switch management
    #=========================================
    
    def logical_state_pins (self, list_of_switch_name) :
        """ 
        Returns the logical state of the three switches in the form of a dictionary of  "Key, values" pairs
                Where key is the switch name and value the logical state of pin associated with the switch.
                The dictionary contains as many pairs as valid and different switch names requested in the input parameter
        
        list_of_switch_name : 
            The types allowed or prohibited for the input parameter
               ** A str     : In this case, only one switch name is allowed. It will then be either "sw1" or "sw2" or "sw3".
               ** A tuple   : NOT ALLOWED
               ** A list    : In this case this list must contain one or more switch names
                              among the three possible: "sw1" and/or "sw2" and/or "sw3".
                              The order is unimportant, and the accidental repetition of a name is of no consequence.

            Reminder: Be careful when using the print statement. 
                      Don't forget to alternate between double quotes and single quotes.
                      print( f"states are { x.logical_state_pins( ['sw1', 'sw3'] ) } " )
                      print( f'states are { x.logical_state_pins( ["sw1", "sw3"] ) } ' )
 
            REMARK : If   the name of the switch is not among the three authorized
                     Then a <KeyError>  will be raised 

        Return : The state value is in three forms
                  ** "ON"  which means <the switch is in the pressed state>
                  ** "OFF" which means <the switch is in the released state>
                  ** None  which means <the switch has not been initialized>, the request has no meaning
                 
                  Exemples : whit state ::= "ON" or "OFF" or None
                     
                  input is a string
                     logical_state_pins( "sw1" ) return  { "sw1", state} 

                  input is a tuple
                     logical_state_pins( ("sw1", "sw3") ) return a dictionary { "sw1":state, "sw3":state }

                  input is a liste
                     logical_state_pins( ["sw1", "sw3"] ) return a dictionary { "sw1":state, "sw3":state }

        """ 
        dico = {}

        # If   the input parameter 'P' is of type <str>
        # Then there is recursion with as input parameter a list containing only the element 'P'
        if isinstance(list_of_switch_name, str):
            dico = self.logical_state_pins( [list_of_switch_name] )

        else :
            for switch_name in list_of_switch_name:
                # here if    the name of the switch is not among the three authorized
                #      then  a <KeyError> error will be raised
                pin = self.DICO_SWITCH_NAME_TO_PIN_CODE[switch_name]

                try:
                    #Here, if the pin has not been initialized (input/output) a RuntimeError will be raised
                    state = GPIO.input(pin)

                except RuntimeError:
                    # The ON/OFF status request has no meaning
                    dico[switch_name] = None 

                else:
                    dico[switch_name] = "ON" if state == self.ON else "OFF"

        return dico

    #----------------------------------------
    def add_event_detect_switch( self, switch_name, trigger = GPIO.FALLING, callback = empty , bouncetime = 50):
        """
        Create a thread that waits for an event to occur on one of the push buttons it is responsible for.
        When the event occurs, the tread calls the callback function, then resumes monitoring

        switch_name   ::= (str) in [ "sw1", "sw2", "sw3" ]

        trigger       ::= (int) in [GPIO.FALLING, GPIO.RISING, GPIO.BOTH] 
                          specifies on which edge of the signal the thread calls the processing function

        callback      ::= <class 'function'>
                          The default name is /empty/ it is the name of a function internal  to the class which does nothing (pass)  
                          Name of the function that will be called by the thread to process the event.
                          The name of the processing function is not a string.
                          Therefore, it should not be written in quotes or double quotes, as strings usually are.

        boucetime     ::= (int) time in milliseconds
                          Waiting time necessary to stabilize the change of state of the push button.
                          The default value is fixed at 50ms
                          Decreasing this value may result in more than one call to the processing function for a single action on the push button.
                          Increasing this value delays the processing of the push button action
        """    
        try:
            pin_of_switch = self.DICO_SWITCH_NAME_TO_PIN_CODE[switch_name]

        except KeyError:

            Buttons.title ( 50, " MESSAGE FROM Maker-pHAT " ) 
            print( f"The reference of switch is > {switch_name} < This value is not compliant." )
            print( f"The reference must belong to the following set : {self.T_SWITCH_NAME}" )
            print(  "Please eliminate the cause of the error" )

            Buttons.title( 50, " STACK CONTENTS " )
            print( traceback.print_stack() )

            Buttons.title( 50, " NO NEED TO GO FURTER ")
            GPIO.cleanup(self.T_SET_CODE_PIN)
            sys.exit()

        else:
            # In order to limit errors as much as possible, the choice was made to carry out the /GPIO.setup/ of the pin 
            #    at the time the method /add_event_detect_switch/ is called.
            # Normally the /add_event_detect_switch/ method is called only once. However, if we wish to change 
            #    the callback function we are assured that the /add_event_detect_switch/ method will not raise an error 
            GPIO.setup(pin_of_switch, GPIO.IN)
            
            # It is not possible to do an /GPIO.add_event_detect/ on a pin if an /GPIO.add_event_detect/ has already been created on this same pin.
            # It is therefore necessary to do a /GPIO.remove_event_detect/ before doing a new /GPIO.add_event_detect/.
            # And in the case where no /GPIO.add_event_detect/ has been created on a pin, it is better to do a preventive /GPIO.remove_detect_event/.
            #    (no risk of raising an error)
            GPIO.remove_event_detect (pin_of_switch)
          
            # Now, All is right
            GPIO.add_event_detect( pin_of_switch, trigger, callback, bouncetime ) 
   


 
    def cleanup( self, switch_names = None):
        """ 
        Has the same behavior as GPIO.cleanup(), but it only acts on the 3 pins assigned to the switchs of Maker-pHAT card
        The normal use of this method is to deactivate a push button.
        To reactivate it it will be necessary to call the setup_switch( switch_name) method before calling the add_event_detect( ... ) method.
        
        list_of_switch_name :  None by default
            ** If not specified, then the three pins are deactivated and placed in a state without risk of destruction for the Raspberry
            ** if type is str then it can  be one and only one of these three values: "sw1" or "sw2' or "sw3"
            ** if type is <class 'list'> then it can be a list or a tuple containing a combination 
                                              of the three character strings: "sw1" or "sw2' or "sw3"
        Remark : When one or more switches have undergone the cleanup operation, it is no longer possible to apply 
                      the add_event_detect function to them.
                  It is necessary to apply the setup_switch function to it before to indicate that the pin 
                      associated with the switch is an input.
        """ 
        if switch_names is None:
            # The 3 pins are disabled
            GPIO.cleanup( self.T_SET_CODE_PIN )

        elif type(switch_names) == str:
            # Only one pin is disabled. The name is placed in a list and the /cleanup/ method is called recursively with this list  
            self.cleanup( [switch_names] )

        else: 
           # Each switch name in the list has its associated pin disabled
           for name in switch_names:
               try: 
                   pin = self.DICO_SWITCH_NAME_TO_PIN_CODE[name]

               except KeyError:
                   Buttons.title ( 50, " MESSAGE FROM Maker-pHAT " ) 
                   print( f"The reference of switch is > {name} < This value is not compliant." )
                   print( f"The reference must belong to the following set : {self.T_SWITCH_NAME}" )
                   print(  "Please eliminate the cause of the error" )
       
                   Buttons.title( 50, " STACK CONTENTS " )
                   print( traceback.print_stack() )
       
                   Buttons.title( 50, " NO NEED TO GO FURTER ")
                   
               else: 
                   GPIO.cleanup( pin )

#======================================
def main():

    buts = Buttons()

    # Declaration of event processing functions (callback function)
    def test_button_sw1(*args):
        print(f"here sw1 processing, args : {args}" )

    def test_button_sw2(*args):
        print(f"here sw2 processing, args[0] : {args[0]}" )

    def test_button_sw3(pin_code):
        print(f"here sw3 processing, pin_code : {pin_code}" )

    def common_test_button_switch(pin_code):
        print(f"COMMON processing : Event on pin_code {pin_code}")

    def rising_event_detected_on_sw1(pin_code):
        buts.add_event_detect_switch("sw1", GPIO.FALLING, falling_event_detected_on_sw1)
        print(f"States : {buts.logical_state_pins('sw1')}")
        print(f"rising_event  : pin {pin_code}" )

    def falling_event_detected_on_sw1(pin_code ):
        buts.add_event_detect_switch("sw1", GPIO.RISING, rising_event_detected_on_sw1)
        print(f"States : {buts.logical_state_pins('sw1')}")
        print(f"falling_event : pin {pin_code}" )



    # Assignment of treads monitoring events occurring on each switch
    # Each switch has its own callback function.
    buts.add_event_detect_switch("sw1", GPIO.FALLING, test_button_sw1)
    buts.add_event_detect_switch("sw2", GPIO.RISING , test_button_sw2)
    buts.add_event_detect_switch("sw3", GPIO.BOTH   , test_button_sw3)


    print("\nYou can now push the button to test them FALLING, RISING, BOTH" )
    time.sleep(7) 

    # Reassign threads monitoring events occurring on each switch
    # All switches have the same callback function.
    buts.add_event_detect_switch("sw1", GPIO.FALLING, common_test_button_switch)
    buts.add_event_detect_switch("sw2", GPIO.RISING , common_test_button_switch) 
    buts.add_event_detect_switch("sw3", GPIO.BOTH   , common_test_button_switch)
    print("\nYou can now push the button to test them with the same callback function")
    time.sleep(7)

    # Now we deactivate all switches
    print("\nCleanup all switch. Now no more reaction from the switches")
    print(f"states befor cleanup : {buts.logical_state_pins(buts.list_of_switch_names)}")
    buts.cleanup(  )
    print(f"states after cleanup : {buts.logical_state_pins(buts.list_of_switch_names)}")
    time.sleep(4)

    # Only callback function of sw1 is activated t_detect_switch/
    print("\nOnly switch SW1 is re-activated. with BOTH trigger. The callback function will be twice callet. Test  it" )
    print(f"States befor add_event_detect_switch : {buts.logical_state_pins(buts.list_of_switch_names)}")
    buts.add_event_detect_switch("sw1", GPIO.BOTH, test_button_sw1)
    print(f"States after add_event_detect_switch : {buts.logical_state_pins(buts.list_of_switch_names)}")
    time.sleep(4)

    # To detect front up and front down
    buts.add_event_detect_switch("sw1", GPIO.FALLING, falling_event_detected_on_sw1)
    print("\nFinally we simulate the BOTH trigger with two callback functions on the sw1")
    time.sleep(7)
    print()


if __name__ == "__main__":
    main()
