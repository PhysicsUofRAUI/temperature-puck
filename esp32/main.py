import json
import network
import socket

# the webpage is currently working
# need to make the form now.
with open('config.json') as json_file:
    config_params = json.load(json_file)

if config_params['ssid'] == "Enter_WiFi_SSID":
    # Create access point and launch webpage to 
    # collect config parameters
    ap = network.WLAN(network.AP_IF)
    ap.active(True)

    while ap.active() == False:
        pass

    # need to define this as a form for people to enter the config params
    def web_page():
        html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
        <body><h1>Hello, World!</h1></body></html>"""
        return html
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        conn_file = conn.makefile('rwb', 0)
        while True:
            line = conn_file.readline()
            if not line or line == b'\r\n':
                break
        response = web_page()
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
else :
    # launch normal operation
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    wlan.connect(config_params['ssid'], config_params['ssid_password'])

    while not wlan.isconnected:
        pass

    # need dict with high and low temps
    
    # need function to check temp
