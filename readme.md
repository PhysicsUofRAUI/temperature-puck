# About
This is a repository to hold all code and KiCAD design files for a 'temperature puck' which is basically a small puck sized, battery powered temperature monitor.

Two versions will be created. One will be WiFi and the other will be LTE-M.

Currently the two sections of code is for the Arduino MKR 1400 (gsm-arduino-code) and the Arduino MKR 1010 (wifi-arduino-code). Development will focus on creating an Android app and refining the prototype to work with it.

# Project Constraints
## WiFi Versions
### Battery Life
- Two years
- must have a warning when it is low on batteries.
- must have a way to replace batteries.

### Messages
Configurable. The user will enter credentials on startup and during that process they will specify a high and low temperature, as well as how often they want a heartbeat sent to them via email.

May look into future integration with common smart home systems such as Google Home, Apple whatever it is, and Home Assitant.

### Size
Puck sized.
- 3" in diameter
- 1" thick

### Price
$35 in BOM costs for a production run of 100 pieces (goal for 6 months of production at full production).

To compete with
- https://tempstick.com/: $140
- https://tempcube.io/: $700
- https://www.thermoworks.com/node/: $75

Both those have more extensive features.

### Temperature Range
-20 to 40 degrees Celsius

### Ingress Protection
IP 52 (probably will need IP 54 since I don't think 52 is common)
Does not nescessarily needs to be tested.
Battery pack location can be IP42 since it must be removable.

### Physical User Interface
- A Qr Code or something similar to allow for the phone app to be connected to the device.
- Device will create a temperary network to allow user to enter network details
- reset button will be located on bottom to allow entering a new network
- contact info

### Warranty
1 year Warranty
