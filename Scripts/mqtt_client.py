# MQTT client demo
# Continuously monitor two different mqtt topics for data
# check if the recieved data matches two predefined commands

import paho.mqtt.client as mqtt

# the callback for when the cleint receives a connack response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Lithial/CoreName")
    client.subscribe("Lithial/CoreTemp")


def on_message(client, userdata, msg):

    #print(type(msg.payload))
    #print(msg.topic + " " + str(msg.payload))

    t = msg.topic
    p = msg.payload.decode(encoding='UTF-8')


    #print(f"Topic: {t}")
    #print(f"Payload: {p}")
    if t == "Lithial/CoreName":
       print(f"Core: {p}")

        # Do something
    if t == "Lithial/CoreTemp":
        print(f"Temp: {p}")
        # Do something else


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
