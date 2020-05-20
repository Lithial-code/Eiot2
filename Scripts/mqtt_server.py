import wmi

from time import sleep
import paho.mqtt.publish as publish
import ssl
# look at open hardware monitor
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
# assign the sensor information to a variable
temperature_infos = w.Sensor()




# loop through all the sensors
while True:
    print("starting loop")
    for sensor in temperature_infos:
        # look at the ones related to temperature
        if sensor.SensorType == u'Temperature':
            print("looping sensors")
            # added this. checks if the sensors are the ones we want and prints only there information
            if sensor.Name == "CPU Core #1" or sensor.Name == "CPU Core #2":
                # print to console and then publish the values
                broker = "127.0.0.1"
                port = 8883
                print(sensor.Name)
                print(sensor.Value)

                publish.single(topic="Lithial/CoreName", payload=sensor.Name, hostname=broker, port=port, tls={"ca_certs": "C:\\Users\Lithial\Desktop\Keys\SecondAttempt\ca-cert.pem"})
                publish.single(topic="Lithial/CoreTemp", payload=sensor.Value, hostname=broker, port=port, tls={"ca_certs": "C:\\Users\Lithial\Desktop\Keys\SecondAttempt\ca-cert.pem"})
                print("Publishing complete")
    sleep(10)
