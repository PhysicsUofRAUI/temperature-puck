# About
This is a repository to hold all code and KiCAD design files for a 'temperature puck' which is basically a small puck sized, battery powered temperature monitor.

Two versions will be created. One will be WiFi and the other will be LTE-M.

# Project Constraints
## WiFi Versions
### Battery Life
- Two years
- must have a warning when it is low on batteries.
- must have a way to replace batteries.

### Messages
One update per hour.

### Size
Puck sized.
- 3" in diameter
- 1" thick

### Price
$100

To compete with
- https://tempstick.com/: $290
- https://tempcube.io/: $700

Both those have more extensive features.

### Temperature Range
0 to 40 degrees Celsius

### Ingress Protection
IP 52 (probably will need IP 54 since I don't think 52 is common)
Does not nescessarily needs to be tested.
Battery pack location can be IP42 since it must be removable.

### Physical User Interface
- A Qr Code or something similar to allow for the phone app to be connected to the device.
- Device will create a temperary network to allow user to enter network details
- reset button will be located on bottom to allow entering a new network
- contact info

### App Functions
- Set Alarms that will create a push notifications.
- View the latest temperature
- view a previous temperatures (by default store one month of data on phone, but allow user to change)
- Allow users to submit feedback through app

### Connection and Data Privacy
- MQTT will be used and secured using standard methods
- the physical device will be needed to connect to the server (via QR code or similar)
- MQTT relay server will be made available throughout lifetime at no additional cost (will investigate cost furter)

### Warranty
1 year Warranty
