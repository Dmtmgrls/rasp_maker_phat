# rasp_maker_phat

[README in english](./EN_README.md)

### Que fait ce package ?
<details>
<summary>rasp_maker_phat contient toutes les classes Python necessaires à la gestion de la carte "chapeau"  MAKER-pHAT.<br>Cette carte est fabriquée par la sociétée Cytron (https://www.cytron.io)</summary><br>           
   
Exemple de montage sur des modules Raspberry Pi 3B+ ou Pi Zero.<br><br>

![](./maker-pHat-card-monted.png )

</details>


### Caractéristiques de cette carte.
<details>
<summary>Cette carte comporte huit LEDs, un buzzer, et trois bouttons poussoires.<br><br></summary>

>- Sa taille est celle d'un module Raspberry Pi Zéro. Elle s'intègre parfaitement à la série Pi Zero de type SBC<br>
(SBC :de l'anglais single-board computer. Ordinateur mono-carte )<br>
>- Elle est également compatible avec les tailles des Raspberry Pi: <br>
>   - Taille standard : 3B/3B+/4B1GB/4B2GB/4B4GB<br>
>   - Taille medium : 3A+<br>
>   - taille small : Pi Zero/W/WH..<br>
>- Elle s'embroche et est totalement compatible avec le Bus GPIO des modules Raspberry.
>- Les 8 LEDs sont selectables par les broches GPIO (17, 18, 27, 22, 25, 12, 13, 19).<br>
>- Les trois boutons poussoirs sont programmables par les broches GPIO (21,19,20). <br>
>- Le Buzzer est activable sur la broche (GPIO 26).<br>
>- les broches GPIO affectées à chaque fonctionnalité sont bien identifiées (sérigraphiées) sur le circuit imprimé.<br>Incluant SPI, UART, I2C, 5V, 3.3V, et GND.<br>
>- Elle munie d'une entrée USB en tant que entrée 5V ou entrée UART.
>- Sa tension d'entrée USB est de 5v. La source pouvant être un PC, une batterie de secours (power bank) ou un adaptateur secteur.
>- Elle peut fonctionner sans son entrée USB. Elle est alors alimentée par le 5V du BUS du module Raspberry Pi.

 <br><br>
**Pour plus d'information consultez le fabriquant** [CyTRON](https://www.cytron.io/c-raspberry-pi-hat#/-c616/cytron-m11/sort=p.number_sales/order=DESC/limit=20/minPrice=/maxPrice=)<br><br>


![](/Documents/EN_Maker-pHAT_Overview.png)


</details>

## Usage

Ce pacakage contients trois modules qui sont décrits ci-dessous :
<br>Précision : le nom des modules est préfixé par la lettre "m_" comme module.

<details>
  
<summary><b>Module  : m_leds.</b> est chargé de la gestion des 8 LEDs de la carte Maker-pHAT</summary>
<br>

<details>
<summary><b>flash( led_n , tempo = 1.0 )</b> La LED concernée passe de l'état <b>ON</b> à <b>OFF</b> pendant la durée de la 'tempo'.</summary> 
<br>
   
>- **led_n** : index de la led.
>   - int [0, 7] 
>   - led_n = 0 pour la LED à l'extrème droite de la carte Maker-pHAT
>   - led_n = 7 pour la LED à lextrème gauche de la carte Maker-pHAT<br><br>
>- **tempo** : float, ]0, oo[
>   - Temps (en secondes) pendant lequel la Led 'n' sera ON. Après ce délais elle passe à l'état OFF.<br>
      Par défaut 'tempo' = 1.0 secondes<br><br>   
</details>

<details>
<summary><b>flash_mask( mask = 0xFF, tempo = 1.0 )</b> La ou les LEDs concernées passent de l'état <b>ON</b> à <b>OFF</b> pendant la durée de la 'tempo'.</summary> 
<br>    

>- **mask** : masque de 8 bits, chaque bit est associé à une Led .
>   - int [0x00, 0xFF] 
>   - mask = 0x01 est associé à la LED située à l'extrème droite de la carte Maker-pHAT
>   - mask = 0x80 est associé à la LED située à l'extrème gauche de la carte Maker-pHAT
>   - mask = 0b01010101 = 0x55 est associé aux LEDS d'index {6, 4, 2, 0}
>   - mask = 0xFF est associé aux LEDS d'index {7, 6, 5, 4, 3, 2, 1, 0}<br><br>
>- **tempo** : float, ]0, oo[
>   - Temps (en secondes) pendant lequel la ou les LEDs du mask seront à ON. Après ce délais ces mêmes LEDs seront à l'état OFF.<br>
      Par défaut tempo = 1.0 secondes<br><br>
</details>


<details>
<summary><b>set_on_leds( mask = 0x00)</b> La ou les LEDs concernées passent à l'état <b>ON<b>.</b></b></summary> 
<br>    

>- **mask** : masque de 8 bits, chaque bit est associé à une Led.
>   - int [0x00, 0xFF] 
>   - mask = 0x01 est associé à la LED située à l'extrème droite de la carte Maker-pHAT
>   - mask = 0x80 est associé à la LED située à l'extrème gauche de la carte Maker-pHAT
>   - mask = 0b01010101 = 0x55 est associé aux LEDS d'index {6, 4, 2, 0}
>   - mask = 0xFF est associé aux LEDS d'index {7, 6, 5, 4, 3, 2, 1, 0}<br><br>
>   - **REMARQUE 1** : si mask = 0x00 alors l'état des 8 LEDs ne sera pas modifié.
>   - **REMARQUE 2** : si une LED concerné par le masque est à l'état **ON**, alors l'état reste à **ON**.

</details>

<details>
<summary><b>set_off_leds( mask = 0x00)</b> La ou les LEDs concernées passent à l'état <b>OFF</b>.</summary> 
<br>    

>- **mask** : masque de 8 bits, chaque bit est associé à une Led.
>   - int [0x00, 0xFF] 
>   - mask = 0x01 est associé à la LED située à l'extrème droite de la carte Maker-pHAT
>   - mask = 0x80 est associé à la LED située à l'extrème gauche de la carte Maker-pHAT
>   - mask = 0b01010101 = 0x55 est associé aux LEDS d'index {6, 4, 2, 0}
>   - mask = 0xFF est associé aux LEDS d'index {7, 6, 5, 4, 3, 2, 1, 0}<br><br>
>   - **REMARQUE 1** : si mask = 0x00 alors l'état des 8 LEDs ne sera pas modifié.
>   - **REMARQUE 2** : si une LED concerné par le masque est à l'état **OFF**, alors l'état reste à **OFF**.

</details>



<details>
<summary><b>Exemple de code</b></summary> 
<br>  

```python
from rasp_maker_phat import m_leds as mleds

# Instantiation de la classe
leds= mleds.Leds()

# Allume la Led N°2 pendant une seconde (par défaut) puis la Led N°5 pendant 0.3secondes.
leds.flash( 2 )
leds.flash( 2, 0.3 )

# Etteinds toutes les LEDs puis n'allumes que les Leds d'index impair.
leds.set_off_leds( x0FF )
leds.set_on_leds( x055 )

# Etteind toutes les LEDs puis allumes pendant 1,5 seconde toutes les LEDs impaires
# puis allumes pendant 2,6 secondes les toutes les LED paires
leds.set_off_leds( x0FF )
leds.flash_mask( x055, 1.5 )
leds.flash_mask( x0AA, 2.6 )
``` 
</details>

`_______________________________________________________________________________`
</details>


<details>
  
<summary><b>Module  : m_buttons.</b> est chargé de la gestion des 3 Boutons poussoir de la carte Maker-pHAT</summary>
<br>

Role : gérer l'ensemble des 3 boutons poussoir (switchs) de la carte chapeau.
<br>

```python
from rasp_maker_phat import m_buttons as mbts

# Instanciation
mbts = mbuttons.Buttons()

# Nous déclarons les 3 fonctions associées à chaque bouton pousoir (B.P.).
# Elles seront chargées de traiter l'évènement survenant sur le B.P. qui lui est affecté. 
# Pour l'exemple, le traitement de l'évènement consiste à afficher le nom de la fonction.

def event_processing_sw1(dummy):
  print("event_processing_sw1")

def event_processing__sw2(dummy):
  print("event_processing_sw2")

def event_processing_sw3(dummy):
  print("event_processing_sw3")

# Pour chaque bouton nous déclarons :
#   Le type d'évènement déclencheur.
#   Le nom de la fonction de traitement de cet évènement
# Le type de traitement est à choisir parmis : GPIO.FALLING or GPIO.RISING or GPIO.BOTH

mbts.add_event_detect_sw1(GPIO.FALLING, event_processing_sw1)
mbts.add_event_detect_sw2(GPIO.RISING, event_processing_sw2)
mbts.add_event_detect_sw3(GPIO.BOTH, event_processing_sw3)
```

</details>

<details>
  
<summary><b>Module  : m_buzzer.</b> Chargé de la gestion de l'unique buzzer de la carte Maker-pHAT</summary>
<br>

Role : gérer l'unique buzzer de la carte chapeau.
<br>

```python
from rasp_maker_phat import m_buzzer as mb

# Instentiation of class Buzzer
buz = mb.buzzer()

# Buzzer ON durant une seconde ( par défaut)
buz.beep(1)

# Buzzer ON durant 0,2 seconde
buz.beep(0.2)

# Fonctionnement cyclique du buzzer
#    Cycle : ON pendant 0,1 seconde, et OFF pendant 0,2 seconde.
#    Ce cycle est répété 5 fois
buz.beep_repeat( 5, 0.1, 0.2)

``` 
</details>

## Contribution
Les "Pull requests" sont les bienvenues.<br>
Pour les changements majeurs, veuillez d'abord ouvrir une question
pour discuter de ce que vous souhaitez changer.<br>
Veillez à mettre à jour les tests le cas échéant.

## License

[MIT](https://choosealicense.com/licenses/mit/)


