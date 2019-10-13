# TB6600 Stepper Motor Driver - RaspberryPi Python

## Overview

The TB6600 is a high voltage 2 phase stepper motor driver with current control. The driver microsteps up to 32 steps, outputs 3.5A to motors, and takes up to 42V of VCC.  This makes the TB6600 an ideal candidate for high power and high precision applications. The 5V input current is ideal for RaspberryPi and Arduino applications. 

Finding documentation for the TB6600 Stepper Motor Driver was challenging due to limited online resources. In fact, some online resources are incorrect. 

 This repo serves as tested and verified working documentation for the TB6600 stepper motor driver. 
 
## TB6600 Operating Warnings 

**Warnings:** 
 - Do not plug/unplug **Signal** or **A/B Stepper Motor Pole High Voltage** connections when current is running through the driver. **This will risk bricking your driver.** (Unconfirmed if Signal or A/B High Voltage outputs are the source of this, however from testing I can confirm that changing these with current will brick your driver)
 - Ensure that connections are secure when running as insecure connections can trigger the above. 
 - Ensure the output amperage and voltage (under High Voltage) do not exceed the limits of the stepper motors 
 - Ensure Signal and High Voltage ground wires are attached to their respective ground pins. It's easy to mix these connections and can be fatal. 
 - At high voltages, pay attention to temperature and make ensure proper thermal conditions (large heatsink) 

## Usage

### Wiring 

So far this is the only surefire wiring with 100% success rate of stepper motor drivers: 
![enter image description here](https://imgur.com/1XneKeX.png)
Use dip switches (sw1-sw6) to select output amperage and microstepping mode. 

RaspberryPi GPIO wiring is given with the following image: 

### Software 

> Coming soon



