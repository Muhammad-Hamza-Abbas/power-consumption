import paho.mqtt.client as mqtt
from random import randrange, uniform
import paho.mqtt.subscribe as subscribe


import time
topics = ['counter']



client = mqtt.Client("Temperature")
client.username_pw_set(username="ali", password="verygood")
client.connect("192.168.1.9", 1883, 60)
m = subscribe.simple(topics, hostname="192.168.1.9", auth = {'username':"ali", 'password':"verygood"})


while True:
    for a in m:
        print(a.topic)
        print(a.payload)
        
    randNu = uniform(20.0, 35.0)
    client.publish("Temperature", randNu)
    print("Just Published" + str(randNu) + "to Topic Temperature")
    time.sleep(1)