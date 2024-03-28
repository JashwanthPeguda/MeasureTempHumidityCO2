import time
import network
import random
from umqtt.simple import MQTTClient
import dht
import machine

# Network credentials
WIFI_SSID = 'Wokwi-GUEST'
WIFI_PASSWORD = ''

# ThingSpeak Channel credentials
CHANNEL_ID = '2488700'
WRITE_API_KEY = '0HNH4COOKXISORZZ'

#ThingSpeak MQTT Server Parameters
mqtt_client_id = "Ny8qKDwZITYSIAM5NzQWMjs"
mqtt_user     = "Ny8qKDwZITYSIAM5NzQWMjs"
mqtt_password  = "WJx30kmsF75L4612ECcOwY0z"
mqtt_server = "mqtt3.thingspeak.com"
mqtt_port = 1883
mqtt_topic_temp = "channels/2488700/publish/fields/field1"
mqtt_topic_humid = "channels/2488700/publish/fields/field2"
mqtt_topic_co2= "channels/2488700/publish/fields/field3"



# Initialize DHT22
dht_sensor = dht.DHT22(machine.Pin(32))  

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print('Network connected!')

# Publish sensor data to ThingSpeak
def publish_sensor_data(temp, humid, co2):
    client = MQTTClient(mqtt_client_id, mqtt_server, port = mqtt_port, user=mqtt_user, password=mqtt_password, keepalive=30)
    client.connect()
    #base_topic = b"channels/" + CHANNEL_ID.encode() + b"/publish/" + WRITE_API_KEY.encode()
    #payload = "field1={}&field2={}&field3={}".format(temp, humid, co2)
    #client.publish(base_topic, payload)
    client.publish(mqtt_topic_temp, str(temp))
    client.publish(mqtt_topic_humid,str(humid))
    client.publish(mqtt_topic_co2,str(co2))
    print("Publishing message Temperatue:", temp)
    print("Publishing message Humidity:", humid)
    print("Publishing message CO2:",co2)
    client.disconnect()


# Read DHT22 sensor and simulate CO2 readings
def read_sensors_and_publish():
    connect_wifi()  # Connect to Wi-Fi
    while True:
        try:
            dht_sensor.measure()
            temp = dht_sensor.temperature()  # Temperature in Celsius
            humid = dht_sensor.humidity()  # Humidity in %
            co2 = random.randint(300, 2000)  # Simulate CO2 in ppm

            print('Publishing data: Temperature: {:.2f}°C, Humidity: {:.2f}%, CO2: {}ppm'.format(temp, humid, co2))
            publish_sensor_data(temp, humid, co2)
        except OSError as e:
            print('Failed to read from DHT sensor.')

        time.sleep(10)  

read_sensors_and_publish()
