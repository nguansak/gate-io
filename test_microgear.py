import microgear.client as microgear
import time
import logging

appid = "c65a518c-4a4b-4fb1-82e5-f5f6bb24a23b"
gearkey = "EgpkLcWDv6wLutj6FjzzX92Gvr1hR36q"
gearsecret =  "pgl-(a##r9eE2JO6o()Bsq4~Wz1)cWOT"

microgear.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    logging.info("Now I am connected with netpie")

def subscription(topic,message):
    logging.info(topic+" "+message)

def disconnect():
    logging.debug("disconnect is work")

microgear.setalias("doraemon")
microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe("/mails")
microgear.connect(False)

while True:
	if(microgear.connected):
		microgear.chat("doraemon","Hello world."+str(int(time.time())))
		print("a")
	time.sleep(3)