**# MeasureTempHumidityCO2**
This project involves the creation of device using an ESP32 microcontroller and a DHT22 sensor. The device measures temperature, humidity, and simulates CO2 levels in the environment. It periodically sends these data points to ThingSpeak using MQTT protocol

**Objectives**
To develop an IoT solution for real-time temp,humidity,CO2 monitoring .
To demonstrate the integration of IoT devices with cloud platforms for data analysis.
To provide a hands-on example of working with sensors, microcontrollers, and MQTT protocol.

**Implementation**
**Hardware Components**
ESP32 Development Board: Serves as the central processing unit, managing sensor data collection and internet communication.
DHT22 Sensor: Measures ambient temperature and humidity.

**Software and Libraries**
MicroPython: Chosen for its ease of use on microcontrollers, facilitating rapid development and prototyping.
MQTT Protocol (umqtt.simple library): Manages data transmission to ThingSpeak.
DHT Library: Interfaces with the DHT22 sensor to read environmental data.
The system's core functionality involves periodic readings of temperature and humidity from the DHT22 sensor, alongside simulated CO2 levels. These readings are packaged and sent to ThingSpeak via MQTT
