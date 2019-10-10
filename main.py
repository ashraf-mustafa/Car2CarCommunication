from network import WLAN
from mqtt
import machine import PIN
import time

def sub_cb(topic, msg):
   print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect("MJ", auth=(WLAN.WPA2, "10101010"), timeout=500)

while not wlan.isconnected():
    machine.idle()
print("Connected to Wifi\n")

client = MQTTClient("COM6", "io.adafruit.com",user="###########", password="#########", port=1883)

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="############/feeds/speed")

while True:
    print("Sending ON")
    client.publish(topic="############/feeds/speed", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="############/feeds/speed", msg="OFF")
    client.check_msg()

    time.sleep(1)
