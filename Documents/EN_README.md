# rasp_maker_phat

[README en français](./FR_README.md)

### What does this package do?
<details>
<summary>The <b>rasp_maker_phat</b> package contains all the Python modules necessary for managing the <b>MAKER-pHAT</b> hat card.<br>This card is manufactured by the company Cytron (https://www.cytron.io)</summary><br>           
   
Example of assemblies on modules Raspberry Pi 3B+ ou Pi Zero.<br><br>

![](./maker-pHat-card-monted.png )

</details>


### Features of this card.
<details>
<summary>This card has eight LEDs, one buzzer, three push buttons, and one USB UART interface.<br><br></summary>

>- Its size is the same as that of a Raspberry Pi Zero module. It integrates perfectly with the Pi Zero SBC type series<br>
(SBC :single-board computer)<br>
>- It is also compatible with Raspberry Pi sizes: <br>
>   - Standard size : 3B/3B+/4B1GB/4B2GB/4B4GB<br>
>   - Medium size: 3A+<br>
>   - Small size: Pi Zero/W/WH..<br>
>- Its pinout is fully compatible with the GPIO Bus of Raspberry modules.
>- The 8 LEDs are selectable via the pins  GPIO (17, 18, 27, 22, 25, 12, 13, 19) in BCM mode.<br>
>- The three push buttons are programmable via the pins GPIO (21,19,20) in BCM mode. <br>
>- The Buzzer can be activated on the pin (GPIO 26)  in BCM mode.<br>
>- The GPIO pins assigned to each functionality are clearly identified (screen printed) on the printed circuit.<br>Including SPI, UART, I2C, 5V, 3.3V, et GND.<br>
>- Its USB input acts as a power input and UART ports..
>- Its USB input voltage is 5v. The source can be a PC, a power bank or an AC adapter.<br>
    It can also be powered by the 5V BUS of the Raspberry Pi module.

 <br><br>
**For more information, consult the manufacturer's website** [CyTRON](https://www.cytron.io/c-raspberry-pi-hat#/-c616/cytron-m11/sort=p.number_sales/order=DESC/limit=20/minPrice=/maxPrice=)<br><br>


![](/Documents/EN_Maker-pHAT_Overview.png)


</details>

## Use

This package contains three modules which are described below:
<br>**Note** : the name of the modules is prefixed by "**m_**" meaning **module**.

<details>
<summary><b>Module : m_leds.</b> It is responsible for managing the 8 LEDs of the Maker-pHAT card</summary><br>

>  <details>
>  <summary><b>Methodes</b> :</summary><br> 
>
>>  <details>
>>  <summary><b>flash( led_n , tempo = 1.0 )</b></summary><br>
>>
>>>-  **AIM** : The LED concerned goes to the <b>ON</b> state, then <b>tempo</b> second later goes to the <b>OFF</b> state.<br><br>
>>>-  **PARAMETER** :
>>>    - **led_n** : LED index.
>>>      -  int [0, 7] 
>>>      -  led_n = 0 for the LED on the far right of the Maker-pHAT board.
>>>      -  led_n = 7 for the LED on the far left of the Maker-pHAT board.<br><br>
>>>    - **tempo** : float, ]0, oo[
>>>      -  Time (in seconds) during which the Led 'n' will be **ON**. After this time it goes to the **OFF** state.<br>
>>>         By default **tempo** = 1.0 seconds<br><br>   
>>  </details>
>>
>>  <details>
>>  <summary><b>flash_mask(mask = 0xFF, tempo = 1.0)</b></summary><br>    
>>
>>>-  **AIM** : The LED(s) concerned set **ON** ,  then after the tempo has elapsed,  the same LEDs set **OFF**<br><br>
>>>-  **PARAMETER** :   
>>>    - **mask** : 8-bit mask, each bit is associated with an LED.
>>>      -  int [0x00, 0xFF] 
>>>      -  mask = 0x01 is associated with the LED located on the far right of the Maker-pHAT card.
>>>      -  mask = 0x80 is associated with the LED located on the far left of the Maker-pHAT card.
>>>      -  mask = 0b01010101 = 0x55 is associated with the index LEDS {6, 4, 2, 0}
>>>      -  mask = 0xFF is associated with the index LEDS {7, 6, 5, 4, 3, 2, 1, 0}<br><br>
>>>    - **tempo** : float, ]0, oo[
>>>      -  Time (in seconds) during which the Led 'n' will be **ON**. After this time it goes to the **OFF** state.<br>
>>>         By default **tempo** = 1.0 seconds<br><br>   
>>  </details>
>>
>>  <details>
>>  <summary><b>set_on_leds( mask = 0x00)</b></summary><br>    
>>
>>>-  **AIM** : The LED(s) concerned set **ON**.</b></b>
>>>-  **PARAMETER** :   
>>>    - **mask** : 8-bit mask, each bit is associated with an LED.
>>>      -  int [0x00, 0xFF] 
>>>      -  mask = 0x01 is associated with the LED located on the far right of the Maker-pHAT card.
>>>      -  mask = 0x80 is associated with the LED located on the far left of the Maker-pHAT card.
>>>      -  mask = 0b01010101 = 0x55 is associated with the index LEDS {6, 4, 2, 0}
>>>      -  mask = 0xFF is associated with the index LEDS {7, 6, 5, 4, 3, 2, 1, 0}<br><br>
>>>      -  **NOTE 1**: if mask = 0x00 then the state of the 8 LEDs will not be modified.
>>>      -  **NOTE 2**: if an LED affected by the mask is in the **ON** state, then the state remains at **ON**.
>>  </details>
>>
>>  <details>
>>  <summary><b>set_off_leds( mask = 0x00)</b></summary><br>    
>>
>>>-  **AIM** : The LED(s) concerned set **OFF**.</b></b>
>>>-  **PARAMETER** :     
>>>    - **mask** : 8-bit mask, each bit is associated with an LED.
>>>      -  int [0x00, 0xFF] 
>>>      -  mask = 0x01 is associated with the LED located on the far right of the Maker-pHAT card.
>>>      -  mask = 0x80 is associated with the LED located on the far left of the Maker-pHAT card.
>>>      -  mask = 0b01010101 = 0x55 is associated with the index LEDS {6, 4, 2, 0}
>>>      -  mask = 0xFF is associated with the index LEDS {7, 6, 5, 4, 3, 2, 1, 0}<br><br>
>>>      -  **NOTE 1**: if mask = 0x00 then the state of the 8 LEDs will not be modified.
>>>      -  **NOTE 2**: if an LED affected by the mask is in the **OFF** state, then the state remains at **OFF**.
>>  </details>
>>
>>  <details>
>>  <summary><b>Code example</b></summary><br>  
>>
>>>  ```python
>>>  from rasp_maker_phat import m_leds as leds
>>>  
>>>  # Class instantiation
>>>  leds = leds.Leds()
>>>  
>>>  # Turns on Led #2 for one second (default) then turns on Led #5 for 0.3 seconds.
>>>  leds.flash( 2 )
>>>  leds.flash( 2, 0.3 )
>>>  
>>>  # Turn off all the LEDs then turn on only the odd index LEDs.
>>>  leds.set_off_leds( x0FF )
>>>  leds.set_on_leds( x055 )
>>>  
>>>  # Turn off all LEDs, then turn on all odd LEDs for 1.5 seconds
>>>  # then turn on all even LEDs for 2.6 seconds
>>>  leds.set_off_leds( x0FF )
>>>  leds.flash_mask( x055, 1.5 )
>>>  leds.flash_mask( x0AA, 2.6 )
>>>  ``` 
>>  </details>
>>
>>  `_______________________________________________________________________________`
>  </details>
</details>

<details>
<summary><b>Module : m_buttons.</b> It is responsible for managing the 3 push buttons on the Maker-pHAT card.</summary><br>

>   <details>
>      <summary><b>Getters</b> :</summary> 
>      <br>
>
>>-   **list_of_switch_pins**<br>
>>        return the list of BCM references of the 3 pins associated with the 3 switchs name screen printed of the Maker_pHAT card.<br>
>>-   **list_of_switch_names**<br>
>>        return list of switch names which are screen printed on the maker-pHAT card.<br>
>>-   **dico_switch_name_to_pin_code**<br>
>>        return the dictionary of couples (switch_name, pin_code) where switch_name is the key.<br>
>>-   **dico_pin_code_to_switch_name**<br>
>>        return the dictionary of couples (pin_code, switch_name) where code_pin is the key.<br>
>   </details>
>
>   <details>
>   <summary><b>Methodes</b> :</summary><br>
>
>>  <details>
>>  <summary><b>logical_state_pins (list_of_switch_name)</b> :</summary><br>  
>> 
>>>-  **AIM**<br>
>>>     Returns the logical state of the three switches in the form of a dictionary of three pairs **<Key, value>**.<br>
>>>     Where **Key** is the switch name, and **value** is the **logical state of the pin** associated with the switch.<br>
>>>     The dictionary contains as many pairs as valid and different switch names requested in the input parameter.<br><br>
>>>- **PARAMETER**
>>>   -  **list_of_switch_name** : 
>>>         -   What data types are allowed or prohibited for the input parameter.<br>
>>>              -   is **str**   : In this case, only one switch name is allowed. It will then be either **"sw1"** or **"sw2"** or **"sw3"**..<br>
>>>              -   is **tuple** : **NOT ALLOWED**.<br>
>>>              -   is **list**  : In this case this list must contain one or more switch names among : **"sw1"** and/or **"sw2"** and/or **"sw3"**.<br>
>>>                                 The order does not matter and accidental repetition of a name has no consequences..<br><br>
>>>        -    **Reminder** : <br>
>>>               -   Be careful when using the print statement.<br>
>>>                   Don't forget to alternate between double quotes and single quotes.<br>
>>>                   ```
>>>                   print( f"states are { x.logical_state_pins( ['sw1', 'sw3'] ) } " )
>>>                   print( f'states are { x.logical_state_pins( ["sw1", "sw3"] ) } ' )
>>>                   ```
>>>        -    **Warning** : <br>
>>>              -   If the switch name is not among **"sw1"** or **"sw2"** or **"sw3"** Then a **KeyError** will be raised.<br>
>>>                  Intercepting and handling this error is the responsibility of the user.<br><br>
>>>- **RETURN**<br>
>>>    -  The logical state of a pin takes three forms
>>>         -    String **"ON"**  which means *the switch is in the pressed state*.<br>
>>>         -    String **"OFF"** which means *the switch is in the released state*.<br>
>>>         -    **None**  which means *the switch has not been initialized*, the request has no meaning.<br><br>
>>>    -  examples of allowed syntax
>>>
>>>         -    input is a string.<br> 
>>>              ```
>>>              logical_state_pins( "sw1" ) -->  { "sw1": "ON" }
>>>              logical_state_pins( "sw2" ) -->  { "sw2": None }
>>>              ```
>>>         -    input is a Liste. 
>>>              ```
>>>              logical_state_pins( ["sw3"] ) -->  { "sw3":"OFF" } 
>>>              logical_state_pins( ["sw1", "sw2", "sw3"] ) -->  { "sw1":"ON", "sw2": None, "sw3":"OFF" }
>>>              ```
>>  </details>
>>
>>  <details>
>>  <summary><b>add_event_detect_switch(  switch_name, trigger = GPIO.FALLING, callback = empty , bouncetime = 50)</b> :</summary><br>
>>
>>>-  **AIM**<br>
>>>     Creates a thread that monitors actions performed on switch (**switch_name**) of the Maker-pHat board.<br>
>>>     The action (**trigger**) will consist of pressing or releasing or both.<br>
>>>     As soon as the action appears, the thread will call the function (**callback**) which will process the action on the switch.<br><br>
>>>- **PARAMETERS**
>>>   -  **switch_name** : str in set "**sw1**", "**sw2**", "**sw3**" .<br>
>>>       - This is the name of the switch of the Maker-pHat board that will be monitored by the thread.<br><br>
>>>   -  **trigger** : indicates on which edge of the signal the processing will be triggered.
>>>       - int only three  possible values [GPIO.FALLING (press), GPIO.RISING (release) , GPIO.BOTH (press or realease] 
>>>       - All actions on a switch will trigger processing either on the rising edge of the signal, or on the falling edge, or both.<br>
>>>         In the latter case the processing will be triggered twice.<br><br>
>>>   - **callback** : this parameter is the name of the function that will be called by the thread to process the event.<br>
>>>      - The default name is **empty**.<br>
>>>        It is a function internal to the class, and this function does nothing (pass).
>>>      - If you do not redefine the callback setting, a tread will still be created.<br>
>>>        When an event occurs, the **empty** function will be called but will produce no effect.<br>
>>>      - **Warning** :<br>
>>>        The name of the processing function is not a string.<br>
>>>        Therefore, it should not be written in quotes or double quotes, as strings usually are.
>>>        <br><br>
>>>   - **bouncetime** : time required to stabilize the state of the push button.
>>>      - int [0,oo[.<br>
>>>      - The unit is milliseconds. By default, its value is set to 5O ms. <br>
>>>      - **Reducing** this value risks making the treatment behavior unstable.<br>
>>>        There is a risk that for a single action the processing will then be launched several times in succession.<br>
>>>      - **Increasing** this value delays the processing of the push button action.<br><br>  
>>  </details>
>>  
>>  <details>
>>  <summary><b>cleanup (switch_names = None)</b> :</summary> 
>>  <br>
>>     
>>>-  **AIM**<br>
>>>       -  The switch(es) mentioned in the parameter (switch_names) will result in:
>>>           - The deactivation of each of the pins associated with these switches.
>>>           - Putting pins in an electrical state which does not entail any risk of destruction of the Raspberry card
>>>           - Stopping and destroying the threads concerned.
>>>       - After this command, all actions on the switches concerned will no longer have any effect..<br><br>
>>>-  **PARAMETER**<br>
>>>       -  **switch_name** : Several writings and types are possible.<br><br>
>>>           - If this parameter is not specified, then its default value will be **None**<br>
>>>             In this case the three switches **sw1**" and "**sw2**" and "**sw3**" will be cleaned.<br>
>>>             After this command, any actions on any switches of the Maker-pHAT card will have no effect.<br><br>
>>>           - str **sw1**" or "**sw2**" or "**sw3**". Only one switch name at a time will be cleaned.<br><br>
>>>           - List or Tuple must contain only the terms **"sw1"** and/or **"sw2"** and/or **"sw3"**<br>
>>>             **Remark**<br>
>>>                -   Writing [ "sw1", "sw2", "sw3" ] is equivalent to not entering a value for this parameter (None case).<br>
>>>                -   The order of the switch names in the list does not matter.<br>
>>>                -   An accidental repetition of a switch name has no consequences.<br>
>>>                    At the first occurrence of the switch name, it will be cleaned.<br><br>
>>  </details>
>>
>>  <details>
>>  <summary><b>Details about writing callback functions</b> :</summary> 
>>  <br>
>>
>>> <details>
>>> <summary><b>how many formats are allowed ? :</b> :</summary> 
>>> <br>
>>> 
>>>   
>>>>  ```python
>>>>  # First possible format
>>>>  # args is a tuple always contains only one element.
>>>>  # This element is the code BCM of the pin causing the event, and **args[0]** is the value of this pin code.
>>>>  def your_function_name(*args):
>>>>      pin_code = args[0]
>>>>      your code
>>>>  
>>>>  # Second possible format
>>>>  # pin_code is the code BCM of the pin causing the event
>>>>  def your_function_name(pin_code):
>>>>      your code
>>>>  ```
>>> </details>
>>>
>>> <details>
>>> <summary><b>how many callback functions should we create ? :</b> :</summary> 
>>> <br>
>>>>     
>>>>  ```python
>>>>  # FIRST POSSIBILIY
>>>>  #    One function per switch you want to monitor, for exemple sw1 and sw3
>>>>  #    In this case the input parameter is unimportant since it is known in advance, but
>>>>  #    the format of this parameter must be indicated even if it will not be used in your code
>>>>  
>>>>  def name_of_your_SW1_callback_function(chosen_parameter_format):
>>>>      your code to process the sw1 switch
>>>>  
>>>>  def name_of_your_SW3_callback_function(chosen_parameter_format):
>>>>      your code to process the sw3 switch
>>>>  #-----------------------------------------------------------
>>>>  
>>>>  # SECOND POSSIBILIY
>>>>  #     Only one function common to all switches.
>>>>  #     It is your code which will adapt the processing according to the input parameter, whatever its format
>>>>  def name_of_your_COMMON_callback_function(pin_code) :
>>>>      if pin_code == PIN_CODE_SW1 :
>>>>         your code for switch sw1
>>>>  
>>>>      elif pin_code == PIN_CODE_SW2 :
>>>>         your code for switch sw2
>>>>  
>>>>      elif pin_code == PIN_CODE_SW3 :
>>>>         your code for switch sw3
>>>>  
>>>>      else :
>>>>         your code for Error (normally this case is impossible)
>>>>  ```
>>> </details>
>>>
>>> <details>
>>> <summary><b>How to process events in the case where trigger == GPIO.BOTH ? :</b> :</summary> 
>>> <br>
>>>   
>>>>   You will not get any information about the action on the switch.<br>
>>>>   Is this a press or a release of the switch? Impossible to know.<br>
>>>>   The input parameter of your callback function will not contain this information, it will only contain the pin code.
>>>>   <br>
>>>>
>>>>  ```python
>>>>  
>>>>  # SIMPLEST CASE
>>>>  #    You do not care whether the triggering of the call is due to a pressing or releasing action on the switch.
>>>>  #    For exemple on sw1 switch, and regardless of the type of triggering event
>>>>  
>>>>  def name_of_your_BOTH_callback_function_on_SW1(chosen_parameter_format):
>>>>      x.your code for switch sw1 
>>>>  
>>>>  #-----------------------------------------------------------
>>>>  
>>>>  
>>>>  
>>>>  # SLIGHTLY LESS SIMPLE CASE
>>>>  #    Depending on the logical state of the switch you select the processing planned for the appropriate type of event
>>>>  
>>>>  def name_of_your_BOTH_callback_function_on_SW1(chosen_parameter_format):
>>>>      if x.logical_state_pins( 'sw1' ) == "ON"  :
>>>>          x.your code for switch sw1 on FALLING edge
>>>>
>>>>      elif x.logical_state_pins( 'sw1' ) == "OFF" :
>>>>          x.your code for switch sw1 on RISING edge   
>>>>
>>>>      else :  # None case but it is imposible
>>>>          pass
>>>>  
>>>>  #-----------------------------------------------------------
>>>>  
>>>>  
>>>>     
>>>>  # MORE COMPLEX CASE
>>>>  #     You must use two callback functions
>>>>  #     -- One for the action of pressing the switch. 
>>>>  #     -- Another when the action disappears.
>>>>  #     The principle is that each callback function deactivates itself and activates the opposite callback function.
>>>>  #     These are two mirror functions
>>>>  #
>>>>  #     Exemple for the switch sw3 (inst_button)
>>>>  
>>>>  inst_buttons = buttons.Buttons()
>>>>  
>>>>  def name_of_your_FALLING_callback_function_SW3(pin_code) :
>>>>      # you deactivate the callback function processing the FALLING trigger, and activate the callback function processing the RISING trigger
>>>>      # The Buttons class allows you to do this in a single command
>>>>      inst_buttons.add_event_detect_switch(  "sw3", GPIO.RISING, name_of_your_RISING_callback_function_SW3 )
>>>>  
>>>>      # your specific code for FALLING event start here
>>>>      your code ....
>>>>  
>>>>  
>>>>  def name_of_your_RISING_callback_function_SW3(pin_code) :
>>>>      # you deactivate the callback function processing the RISING trigger, and activate the callback function processing the FALLING trigger
>>>>      # The Buttons class allows you to do this in a single command
>>>>      inst_buttons.add_event_detect_switch( "sw3", GPIO.FALLING, name_of_your_FALLING_callback_function_SW3)
>>>>  
>>>>      # your specific code for RISING event start here
>>>>      your code  ....     
>>>>  ```
>>>>  </details>
>>>> 
>>>  </details>
>>>  
>>>  <details>
>>>  <summary><b>Code example</b></summary> 
>>>  <br>  
>>>     
>>>>  ```python
>>>>    buts = Buttons()
>>>>
>>>>    # Declaration of event processing functions (callback function)
>>>>    def test_button_sw1(*args):
>>>>        print(f"here sw1 processing, args : {args}" )
>>>>
>>>>    def test_button_sw2(*args):
>>>>        print(f"here sw2 processing, args[0] : {args[0]}" )
>>>>
>>>>    def test_button_sw3(pin_code):
>>>>        print(f"here sw3 processing, pin_code : {pin_code}" )
>>>>
>>>>    def common_test_button_switch(pin_code):
>>>>        print(f"COMMON processing : Event on pin_code {pin_code}")
>>>>
>>>>    def rising_event_detected_on_sw1(pin_code):
>>>>        buts.add_event_detect_switch("sw1", GPIO.FALLING, falling_event_detected_on_sw1)
>>>>        print(f"States : {buts.logical_state_pins('sw1')}")
>>>>        print(f"rising_event  : pin {pin_code}" )
>>>>
>>>>    def falling_event_detected_on_sw1(pin_code ):
>>>>        buts.add_event_detect_switch("sw1", GPIO.RISING, rising_event_detected_on_sw1)
>>>>        print(f"States : {buts.logical_state_pins('sw1')}")
>>>>        print(f"falling_event : pin {pin_code}" )
>>>>
>>>>
>>>>
>>>>    # Assignment of treads monitoring events occurring on each switch
>>>>    # Each switch has its own callback function.
>>>>    buts.add_event_detect_switch("sw1", GPIO.FALLING, test_button_sw1)
>>>>    buts.add_event_detect_switch("sw2", GPIO.RISING , test_button_sw2)
>>>>    buts.add_event_detect_switch("sw3", GPIO.BOTH   , test_button_sw3)
>>>>
>>>>
>>>>    print("\nYou can now push the button to test them FALLING, RISING, BOTH" )
>>>>    time.sleep(7)
>>>>
>>>>    # Reassign threads monitoring events occurring on each switch
>>>>    # All switches have the same callback function.
>>>>    buts.add_event_detect_switch("sw1", GPIO.FALLING, common_test_button_switch)
>>>>    buts.add_event_detect_switch("sw2", GPIO.RISING , common_test_button_switch)
>>>>    buts.add_event_detect_switch("sw3", GPIO.BOTH   , common_test_button_switch)
>>>>    print("\nYou can now push the button to test them with the same callback function")
>>>>    time.sleep(7)
>>>>
>>>>    # Now we deactivate all switches
>>>>    print("\nCleanup all switch. Now no more reaction from the switches")
>>>>    print(f"states befor cleanup : {buts.logical_state_pins(buts.list_of_switch_names)}")
>>>>    buts.cleanup(  )
>>>>    print(f"states after cleanup : {buts.logical_state_pins(buts.list_of_switch_names)}")
>>>>    time.sleep(4)
>>>>
>>>>    # Only callback function of sw1 is activated t_detect_switch/
>>>>    print("\nOnly switch SW1 is re-activated. with BOTH trigger. The callback function will be twice callet. Test  it" )
>>>>    print(f"States befor add_event_detect_switch : {buts.logical_state_pins(buts.list_of_switch_names)}")
>>>>    buts.add_event_detect_switch("sw1", GPIO.BOTH, test_button_sw1)
>>>>    print(f"States after add_event_detect_switch : {buts.logical_state_pins(buts.list_of_switch_names)}")
>>>>    time.sleep(4)
>>>>
>>>>    # To detect front up and front down
>>>>    buts.add_event_detect_switch("sw1", GPIO.FALLING, falling_event_detected_on_sw1)
>>>>    print("\nFinally we simulate the BOTH trigger with two callback functions on the sw1")
>>>>    time.sleep(7)
>>>>    print()
>>>>
>>>>  ```
>>>  </details>
>>>
>>>`_______________________________________________________________________________`
>>  </details>
>
>  </details>

<details>   
<summary><b>Module  : m_buzzer.</b> It is responsible for managing the unique buzzer of the Maker-pHAT card</summary><br>
   
>  <details>
>  <summary><b>Methodes</b> :</summary><br> 
>
>>  <details>
>>  <summary><b>beep (beep_duration = 1.0)</b> :</summary><br>
>>
>>>-  **AIM** :  For a time expressed in seconds, the buzzer emits a sound.<br><br>
>>>-  **PARAMETERS**
>>>      -  **beep_duration** : float in ]0, oo[.<br>
>>>      -  Unit seconds
>>>      -  Default value 1 second.
>>  </details> 
>>
>>  <details>
>>  <summary><b>beep_repeat (number_cycles = 2, beep_duration = 1.0, noiseless_duration = 1.0 )</b> :</summary><br>
>>
>>>-  **AIM**<br>
>>>     Buzzer beeps number_cycles times, and a cycle starts with a beep.<br>
>>>     The buzzer emits a sound for beep_duration seconds and remains silent for noiseless_duration seconds each cycle.<br><br>
>>>- **PARAMETERS**
>>>   -  **number_cycles** : Number of cycle repetitions (beep-silent).<br>
>>>       - int in  [2, 3, .. oo[.<br> 
>>>       - Expressed in seconds <br>
>>>      -  Default value 2.<br><br>
>>>   -  **beep_duration** : Time during which the buzzer emits a sound.<br>
>>>      -  float in ]0, oo[.<br>
>>>      -  Expressed in seconds.<br>
>>>      -  Default value 1.0 second.<br><br>
>>>   -  **noiseless_duration** : Time during which the buzzer remains silent.<br>
>>>      -  float in ]0, oo[.<br>
>>>      -  Expressed in seconds <br>
>>>      -  Default value 1.0 second.<br><br>
>>  </details> 
>>   
>>   <details>
>>   <summary><b>Code Exemple</b> :</summary><br>
>>
>>>  ```python
>>>  from rasp_maker_phat import m_buzzer as mb
>>> 
>>>  
>>>  #create the buz obj from the Buzzer class
>>>  buz = mb.Buzzer()
>>>
>>>  # Buzzer on for one second (default)
>>>  buz.beep()
>>>  time.sleep(1)  # Pause before trying another beep time value
>>>
>>>  # Buzzer on for 0.2 seconds
>>>  buz.beep(0.2)
>>>  time.sleep(1)  # Pause before trying a cycle
>>>
>>>  # Cyclic operation of the buzzer
>>>  # Cycle: ON for 0.1 seconds and OFF for 0.2 seconds.
>>>  # This cycle is repeated 5 times
>>>  buz.beep_repeat(5, 0.1, 0.2)
>>>  ```
>>>
>>>`_______________________________________________________________________________`   
>>  </details>
>  </details>
</details>
 
## Contribution
Pull requests are welcome.<br>
For major changes, please open a question first to discuss what you want to change.<br>
Be sure to update tests as appropriate.<br>

## License

[MIT](https://choosealicense.com/licenses/mit/


