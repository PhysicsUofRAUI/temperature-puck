from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import paho.mqtt.client as mqtt
from datetime import datetime
from config import MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT, MQTT_TOPICS

class MQTTApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.message_label_one = Label(text='Waiting for messages...')
        self.message_label_two = Label(text='Waiting for messages...')
        self.layout.add_widget(self.message_label_one)
        self.layout.add_widget(self.message_label_two)

        # MQTT configuration
        self.broker_address = MQTT_BROKER_ADDRESS
        self.broker_port = MQTT_BROKER_PORT
        self.topics = MQTT_TOPICS
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

        # Set up MQTT callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Connect to the MQTT broker
        self.client.connect(self.broker_address, self.broker_port, 60)

        # Start the MQTT loop in a separate thread
        self.client.loop_start()

        return self.layout

    def on_connect(self, client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT broker")
            # Subscribe to the topic upon successful connection
            # Subscribe to multiple topics
            for topic in self.topics:
                self.client.subscribe(topic)
        else:
            print("Failed to connect to MQTT broker")

    def on_message(self, client, userdata, msg):
        # Callback when a new message is received
        if msg.topic == "Tempdata-kenzie" :
            message = msg.payload.decode("utf-8")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.update_message_one(f"Kenzie's House: {timestamp} - {message}")

        else :
            message = msg.payload.decode("utf-8")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.update_message_two(f"Pump House: {timestamp} - {message}")

    def update_message_one(self, message):
        # Update the label with the received message
        self.message_label_one.text = message

    def update_message_two(self, message):
        # Update the label with the received message
        self.message_label_two.text = message

if __name__ == '__main__':
    MQTTApp().run()
