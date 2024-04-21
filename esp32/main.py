import json
import network
import socket
from microdot import Microdot, send_file

app = Microdot()

# the webpage is currently working
# need to make the form now.
with open('config.json') as json_file:
    config_params = json.load(json_file)

@app.route('/', methods=['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        if 'ssid' in request.form:
            config_params['ssid'] = request.form['ssid']
        if 'ssid_password' in request.form:
            config_params['ssid_password'] = request.form['ssid_password']
        if 'high_temp' in request.form:
            config_params['high_temp'] = request.form['high_temp']
        if 'low_temp' in request.form:
            config_params['low_temp'] = request.form['low_temp']
        if 'email' in request.form:
            config_params['email'] = request.form['email']
        if 'alert_interval' in request.form:
            config_params['alert_interval'] = request.form['alert_interval']

        # update the json file
        with open('config.json') as json_file:
            json.dump(config_params, json_file)
    else:
        return send_file('config_form.html')

if config_params['ssid'] == "Enter_WiFi_SSID":
    # Create access point and launch webpage to 
    # collect config parameters
    ap = network.WLAN(network.AP_IF)
    ap.active(True)

    while ap.active() == False:
        pass

    app.run()

else :
    # launch normal operation
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    wlan.connect(config_params['ssid'], config_params['ssid_password'])

    while not wlan.isconnected:
        pass

    # need dict with high and low temps

    # need function to check temp
