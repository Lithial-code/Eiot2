This in a mosquitto based mqtt project in python.

Dependancies
WMI
PahoMQTT
Mosquitto
SSH
Open Hardware Monitor

It is a pain to install everything to make the advanced copy work but the basic version should work with just OHWM, WMI and the basic install of mosquitto. Maybe anyways.

This project was made for a school project where we needed to create a couple of scripts that would send messages to and from sensors reading temperatures. Moquitto is used as a base to recieve the messages. You need to modify the mosquitto.conf to have the right port, ip and any ssl certificates and then run the whole program using mosquitto -v -c mosquitto.conf. At least this is how i made it work. Maybe one day I'll come back to this to make something cool and a little more automated to set up.
