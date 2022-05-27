# version 4
from random import randint
from asyncio import sleep
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.urls import path
from channels.generic.websocket import AsyncWebsocketConsumer
import paho.mqtt.client as mqtt
from datetime import date, datetime,tzinfo,timedelta
import sys
from .models import Dashboards
import sqlite3
import math

current_time=''

conn = sqlite3.connect('customer.db')
c=conn.cursor()
c.execute("SELECT rowid, * FROM consumption4V3")
items = c.fetchall()
_1fpft=0
_1ftrp= 0
_1frp1=  0
# FRP20.00FRP2_
_1frp2=  0      
# FRP30.00FRP3_
_1frp3= 0
# FTAP0.00FTAP_
_1ftap= 0
# FAP10.00FAP1_
_1fap1= 0
# FAP20.00FAP2_
_1fap2= 0
# FAP30.00FAP3_
_1fap3= 0
# FV10.00FV1_
_1fv1= 0
# FV20.00FV2_
_1fv2= 0
# FV30.00FV3_
_1fv3= 0
# FTP0.00FTP
_1ftp= 0
_1fp1=0
_1fpf1=0
_1fct1=0
_1fp2=0
_1fpf2=0
_1fct2=0
_1fp3=0
_1fpf3=0
_1fct3=0
_1te=0
_1freq=0
_1meterid=0
_1rp1=0
_1rp2=0
_1rp3=0
_1tapr=0
_1rtapr=0
_1aap1r=0
_1aap2r=0
_1aap3r=0
_1trpr=0
_1tce=0
_1tcf=0
meter1a = ''
meter1b = ''

_1ipaddress=''
_1CTfactor=50

_2fpft=0
_2ftrp= 0
_2frp1=  0
# FRP20.00FRP2_
_2frp2=  0      
# FRP30.00FRP3_
_2frp3= 0
# FTAP0.00FTAP_
_2ftap= 0
# FAP10.00FAP1_
_2fap1= 0
# FAP20.00FAP2_
_2fap2= 0
# FAP30.00FAP3_
_2fap3= 0
# FV10.00FV1_
_2fv1= 0
# FV20.00FV2_
_2fv2= 0
# FV30.00FV3_
_2fv3= 0
# FTP0.00FTP
_2ftp= 0
_2fp1=0
_2fpf1=0
_2fct1=0
_2fp2=0
_2fpf2=0
_2fct2=0
_2fp3=0
_2fpf3=0
_2fct3=0
_2te=0
_2freq=0
_2meterid=0
_2rp1=0
_2rp2=0
_2rp3=0
_2tapr=0
_2rtapr=0
_2aap1r=0
_2aap2r=0
_2aap3r=0
_2trpr=0
_2tce=0
_2tcf=0
meter2a = ''
meter2b = ''

_2ipaddress=''
_2CTfactor=50


_3fpft=0
_3ftrp= 0
_3frp1=  0
# FRP20.00FRP2_
_3frp2=  0      
# FRP30.00FRP3_
_3frp3= 0
# FTAP0.00FTAP_
_3ftap= 0
# FAP10.00FAP1_
_3fap1= 0
# FAP20.00FAP2_
_3fap2= 0
# FAP30.00FAP3_
_3fap3= 0
# FV10.00FV1_
_3fv1= 0
# FV20.00FV2_
_3fv2= 0
# FV30.00FV3_
_3fv3= 0
# FTP0.00FTP
_3ftp= 0
_3fp1=0
_3fpf1=0
_3fct1=0
_3fp2=0
_3fpf2=0
_3fct2=0
_3fp3=0
_3fpf3=0
_3fct3=0
_3teI=float(items[-1][2])
_3te=_3teI
_3teArray=[]
_3freq=0
_3meterid=0
_3rp1=0
_3rp2=0
_3rp3=0
_3tapr=0
_3rtapr=0
_3aap1r=0
_3aap2r=0
_3aap3r=0
_3trpr=0
_3tce=0
_3tcf=0
meter1a = ''
meter1b = ''

_3ipaddress=''
_3CTfactor=1
_3todayconsumption=0

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name

GMT = Zone(0,False,'GMT')
PST = Zone(5,False,'PST')


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
   
    client.subscribe("meter1a")
    client.subscribe("meter1b")
    client.subscribe("meter2a")
    client.subscribe("meter2b")
    client.subscribe("meter4a")
    client.subscribe("meter4b")

def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    
    global current_time
    print(current_time)
    global _1fpft
    # FTRP0.00FTRP_
    global _1ftrp
    # FRP10.00FRP1_
    global _1frp1
    # FRP20.00FRP2_
    global _1frp2     
    # FRP30.00FRP3_
    global _1frp3
    # FTAP0.00FTAP_
    global _1ftap
    # FAP10.00FAP1_
    global _1fap1
    # FAP20.00FAP2_
    global _1fap2
    # FAP30.00FAP3_
    global _1fap3
    # FV10.00FV1_
    global _1fv1
    # FV20.00FV2_
    global _1fv2
    # FV30.00FV3_
    global _1fv3
    # FTP0.00FTP
    global _1ftp
    global _1fp1
    global _1fpf1
    global _1fct1
    global _1fp2
    global _1fpf2
    global _1fct2
    global _1fp3
    global _1fpf3
    global _1fct3
    global _1te
    global _1freq
    global _1meterid
    global _1ipaddress
    global _1fv1
    global _1fv2
    global _1fv3
    global _1rp1
    global _1rp2
    global _1rp3
    global _1tapr
    global _1rtapr
    global _1aap1r
    global _1aap2r
    global _1aap3r
    global _1trpr
    global _1tce
    global _1tcf
    global _1CTfactor

    
    global _2fpft
    # FTRP0.00FTRP_
    global _2ftrp
    # FRP10.00FRP1_
    global _2frp1
    # FRP20.00FRP2_
    global _2frp2     
    # FRP30.00FRP3_
    global _2frp3
    # FTAP0.00FTAP_
    global _2ftap
    # FAP10.00FAP1_
    global _2fap1
    # FAP20.00FAP2_
    global _2fap2
    # FAP30.00FAP3_
    global _2fap3
    # FV10.00FV1_
    global _2fv1
    # FV20.00FV2_
    global _2fv2
    # FV30.00FV3_
    global _2fv3
    # FTP0.00FTP
    global _2ftp
    global _2fp1
    global _2fpf1
    global _2fct1
    global _2fp2
    global _2fpf2
    global _2fct2
    global _2fp3
    global _2fpf3
    global _2fct3
    global _2te
    global _2freq
    global _2meterid
    global _2ipaddress
    global _2fv1
    global _2fv2
    global _2fv3
    global _2rp1
    global _2rp2
    global _2rp3
    global _2tapr
    global _2rtapr
    global _2aap1r
    global _2aap2r
    global _2aap3r
    global _2trpr
    global _2tce
    global _2tcf
    global _2CTfactor

    global _3fpft
    # FTRP0.00FTRP_
    global _3ftrp
    # FRP10.00FRP1_
    global _3frp1
    # FRP20.00FRP2_
    global _3frp2     
    # FRP30.00FRP3_
    global _3frp3
    # FTAP0.00FTAP_
    global _3ftap
    # FAP10.00FAP1_
    global _3fap1
    # FAP20.00FAP2_
    global _3fap2
    # FAP30.00FAP3_
    global _3fap3
    # FV10.00FV1_
    global _3fv1
    # FV20.00FV2_
    global _3fv2
    # FV30.00FV3_
    global _3fv3
    # FTP0.00FTP
    global _3ftp
    global _3fp1
    global _3fpf1
    global _3fct1
    global _3fp2
    global _3fpf2
    global _3fct2
    global _3fp3
    global _3fpf3
    global _3fct3
    global _3te
    global _3teI
    global _3teArray
    global _3freq
    global _3meterid
    global _3ipaddress
    global _3fv1
    global _3fv2
    global _3fv3
    global _3rp1
    global _3rp2
    global _3rp3
    global _3tapr
    global _3rtapr
    global _3aap1r
    global _3aap2r
    global _3aap3r
    global _3trpr
    global _3tce
    global _3tcf
    global _3CTfactor
    
    
    if msg.topic=="meter1a":
        meter1a = str(msg.payload, 'UTF-8') 
        
        print('meter1a Values: ' + meter1a)
        # FTRP0.00FTRP_
        _1ftrp= (meter1a[meter1a.find('FTRP')+4:meter1a.find('FTRP_')])
        # FRP10.00FRP1_
        _1frp1= (meter1a[meter1a.find('FRP1')+4:meter1a.find('FRP1_')])
        # FRP20.00FRP2_
        _1frp2= (meter1a[meter1a.find('FRP2')+4:meter1a.find('FRP2_')])
        # FRP30.00FRP3_
        _1frp3= (meter1a[meter1a.find('FRP3')+4:meter1a.find('FRP3_')])
        # FTAP0.00FTAP_
        _1ftap= (meter1a[meter1a.find('FTAP')+4:meter1a.find('FTAP_')])
        # FAP10.00FAP1_
        _1fap1= (meter1a[meter1a.find('FAP1')+4:meter1a.find('FAP1_')])
        # FAP20.00FAP2_
        _1fap2= (meter1a[meter1a.find('FAP2')+4:meter1a.find('FAP2_')])
        # FAP30.00FAP3_
        _1fap3= (meter1a[meter1a.find('FAP3')+4:meter1a.find('FAP3_')])
        # FV10.00FV1_
        _1fv1= (meter1a[meter1a.find('FV1')+3:meter1a.find('FV1_')])
        # FV20.00FV2_
        _1fv2= (meter1a[meter1a.find('FV2')+3:meter1a.find('FV2_')])
        # FV30.00FV3_
        _1fv3= (meter1a[meter1a.find('FV3')+3:meter1a.find('FV3_')])
        # FTP0.00FTP
        _1ftp= (meter1a[meter1a.find('FTP')+3:meter1a.find('FTP_')])

        try:
            # FTRP0.00FTRP_
            _1ftrp= float(_1ftrp)
            # FRP10.00FRP1_
            _1frp1=  float(_1frp1)
            # FRP20.00FRP2_
            _1frp2=   float(_1frp2)       
            # FRP30.00FRP3_
            _1frp3= float(_1frp3)
            # FTAP0.00FTAP_
            _1ftap= float(_1ftap)
            # FAP10.00FAP1_
            _1fap1= float(_1fap1)
            # FAP20.00FAP2_
            _1fap2= float(_1fap2)
            # FAP30.00FAP3_
            _1fap3= float(_1fap3)
            # FV10.00FV1_
            _1fv1= float(_1fv1)
            # FV20.00FV2_
            _1fv2= float(_1fv2)
            # FV30.00FV3_
            _1fv3= float(_1fv3)
            # FTP0.00FTP
            _1ftp= float(_1ftp) *_1CTfactor

            if(math.isnan(_1ftrp)):
                _1ftrp=0
            if(math.isnan(_1frp1)):
                _1frp1=0
            if(math.isnan(_1frp2)):
                _1frp2=0
            if(math.isnan(_1frp3)):
                _1frp3=0
            if(math.isnan(_1ftap)):
                _1ftap=0
            if(math.isnan(_1fap1)):
                _1fap1=0
            if(math.isnan(_1fap2)):
                _1fap2=0
            if(math.isnan(_1fap3)):
                _1fap3=0
            if(math.isnan(_1fv1)):
                _1fv1=0
            if(math.isnan(_1fv2)):
                _1fv2=0
            if(math.isnan(_1fv3)):
                _1fv3=0
            if(math.isnan(_1ftp)):
                _1ftp=0
        except:
            print("2. Error occured while converting to string meter1a")  
            # FTRP0.00FTRP_
            _1ftrp= 0
            # FRP10.00FRP1_
            _1frp1=  0
            # FRP20.00FRP2_
            _1frp2=  0      
            # FRP30.00FRP3_
            _1frp3= 0
            # FTAP0.00FTAP_
            _1ftap= 0
            # FAP10.00FAP1_
            _1fap1= 0
            # FAP20.00FAP2_
            _1fap2= 0
            # FAP30.00FAP3_
            _1fap3= 0
            # FV10.00FV1_
            _1fv1= 0
            # FV20.00FV2_
            _1fv2= 0
            # FV30.00FV3_
            _1fv3= 0
            # FTP0.00FTP
            _1ftp= 0
            

    if msg.topic=="meter1b":
        meter1b = str(msg.payload, 'UTF-8') 
            
        print('meter1b Values: ' + meter1b)
      
        # FPFT0.70FPFT
        _1fpft= (meter1b[meter1b.find('FPFT')+4:meter1b.find('FPFT_')])
        _1te = (meter1b[meter1b.find('FFTE')+4:meter1b.find('FFTE_')])
        _1freq = (meter1b[meter1b.find('FFREQ')+5:meter1b.find('FFREQ_')])
        _1fp1 = (meter1b[meter1b.find('FP1')+3:meter1b.find('FP1_')])
        _1fp2 = (meter1b[meter1b.find('FP2')+3:meter1b.find('FP2_')])
        _1fp3 = (meter1b[meter1b.find('FP3')+3:meter1b.find('FP3_')])
        _1fct1 = (meter1b[meter1b.find('FCT1')+4:meter1b.find('FCT1_')])
        _1fct2 = (meter1b[meter1b.find('FCT2')+4:meter1b.find('FCT2_')])
        _1fct3 = (meter1b[meter1b.find('FCT3')+4:meter1b.find('FCT3_')])
        _1fpf1 = (meter1b[meter1b.find('FPF1')+4:meter1b.find('FPF1_')])
        _1fpf2 = (meter1b[meter1b.find('FPF2')+4:meter1b.find('FPF2_')])
        _1fpf3 = (meter1b[meter1b.find('FPF3')+4:meter1b.find('FPF3_')])
        _1ipaddress = meter1b[meter1b.find('IP')+2:meter1b.find('IP_')]
        _1meterid = meter1b[meter1b.find('MID')+3:meter1b.find('MID_')]
        # totalenergy = float(totalenergy)
        try:
            _1fpft = float(_1fpft)
            _1fp1 = float(_1fp1)*_1CTfactor
            _1fp2 = float(_1fp2)*_1CTfactor
            _1fp3 = float(_1fp3)*_1CTfactor
             
            _1fct1 = float(_1fct1)*_1CTfactor
            _1fct1 = round(_1fct1,2)
            _1fct2 = float(_1fct2)*_1CTfactor
            _1fct2 = round(_1fct2,2)
            _1fct3 = float(_1fct3)*_1CTfactor
            _1fct3 = round(_1fct3,2)
            _1fpf1 = float(_1fpf1)
            _1fpf2 = float(_1fpf2)
            _1fpf3 = float(_1fpf3)
            _1fp3 = round(_1fv3 * _1fct3 * 0.001,2)

            


            if(math.isnan(_1fpft)):
                _1fpft=0
            if(math.isnan(_1fp1)):
                _1fp1=0
            if(math.isnan(_1fp2)):
                _1fp2=0
            if(math.isnan(_1fp3)):
                _1fp3=0
            if(math.isnan(_1fct1)):
                _1fct1=0
            if(math.isnan(_1fct2)):
                _1fct2=0
            if(math.isnan(_1fct3)):
                _1fct3=0
            if(math.isnan(_1fpf1)):
                _1fpf1=0
            if(math.isnan(_1fpf2)):
                _1fpf2=0
            if(math.isnan(_1fpf3)):
                _1fpf3=0

            if(_1fpf1<0.1):
                _1fpf1=_1fpf1*10
            if(_1fpf2<0.1):
                _1fpf2=_1fpf2*10
            if(_1fpf3<0.1):
                _1fpf3=_1fpf3*10
            if(_1fpft<0.1):
                _1fpft=_1fpft*10
            
        except:
            print("2. Error occured while converting to string meter1b")
            _1fpft=0
            _1fp1 = 0
            _1fp2 = 0
            _1fp3 = 0
            _1fct1 = 0
            _1fct2 = 0
            _1fct3 = 0
            _1fpf1 = 0
            _1fpf2 = 0
            _1fpf3 = 0

        print('_1TE: ' + str(_1te))
        print('_1FREQ: ' + str(_1freq))
            # FV10.00FV1_
        print('_1FV1: '+str(_1fv1))
            # FV20.00FV2_
        print('_1FV2: '+str(_1fv2))
            # FV30.00FV3_
        print('_1FV3: '+str(_1fv3))
        print('_1FCT1: ' + str(_1fct1))
        print('_1FCT2: ' + str(_1fct2))
        print('_1FCT3: ' + str(_1fct3))
        print('_1FTP: '+str(_1ftp))
        print('_1FP1: ' + str(_1fp1))
        print('_1FP2: ' + str(_1fp2))
        print('_1FP3: ' + str(_1fp3))
        # FTRP0.00FTRP_
        print('_1FTRP: '+str(_1ftrp))
            # FRP10.00FRP1_
        print('_1FRP1: '+str(_1frp1))            
            # FRP20.00FRP2_
        print('_1FRP2: '+str(_1frp2))
            # FRP30.00FRP3_
        print('_1FRP3: '+str(_1frp3))
            # FTAP0.00FTAP_
        print('_1FTAP: '+str(_1ftap))
            # FAP10.00FAP1_
        print('_1FAP1: '+str(_1fap1))
            # FAP20.00FAP2_
        print('_1FAP2: '+str(_1fap2))
            # FAP30.00FAP3_
        print('_1FAP3: '+str(_1fap3))
        print('_1FPFT: '+str(_1fpft))
        print('_1FPF1: ' + str(_1fpf1))
        print('_1FPF2: ' + str(_1fpf2))
        print('_1FPF3: ' + str(_1fpf3))
        print('_1CT Factor:' +str(_1CTfactor))
        print('_1Ipaddress ' + _1ipaddress)
        print('_1Meter Id ' + _1meterid)

        


    
    if msg.topic=="meter2a":
        meter2a = str(msg.payload, 'UTF-8') 
        print('meter2a Values: ' + meter2a)
        # FTRP0.00FTRP_
        _2ftrp= (meter2a[meter2a.find('FTRP')+4:meter2a.find('FTRP_')])
        # FRP10.00FRP1_
        _2frp1= (meter2a[meter2a.find('FRP1')+4:meter2a.find('FRP1_')])
        # FRP20.00FRP2_
        _2frp2= (meter2a[meter2a.find('FRP2')+4:meter2a.find('FRP2_')])
        # FRP30.00FRP3_
        _2frp3= (meter2a[meter2a.find('FRP3')+4:meter2a.find('FRP3_')])
        # FTAP0.00FTAP_
        _2ftap= (meter2a[meter2a.find('FTAP')+4:meter2a.find('FTAP_')])
        # FAP10.00FAP1_
        _2fap1= (meter2a[meter2a.find('FAP1')+4:meter2a.find('FAP1_')])
        # FAP20.00FAP2_
        _2fap2= (meter2a[meter2a.find('FAP2')+4:meter2a.find('FAP2_')])
        # FAP30.00FAP3_
        _2fap3= (meter2a[meter2a.find('FAP3')+4:meter2a.find('FAP3_')])
        # FV10.00FV1_
        _2fv1= (meter2a[meter2a.find('FV1')+3:meter2a.find('FV1_')])
        # FV20.00FV2_
        _2fv2= (meter2a[meter2a.find('FV2')+3:meter2a.find('FV2_')])
        # FV30.00FV3_
        _2fv3= (meter2a[meter2a.find('FV3')+3:meter2a.find('FV3_')])
        # FTP0.00FTP
        _2ftp= (meter2a[meter2a.find('FTP')+3:meter2a.find('FTP_')])

        try:
            # FTRP0.00FTRP_
            _2ftrp= float(_2ftrp)
            # FRP10.00FRP1_
            _2frp1=  float(_2frp1)
            # FRP20.00FRP2_
            _2frp2=   float(_2frp2)       
            # FRP30.00FRP3_
            _2frp3= float(_2frp3)
            # FTAP0.00FTAP_
            _2ftap= float(_2ftap)
            # FAP10.00FAP1_
            _2fap1= float(_2fap1)
            # FAP20.00FAP2_
            _2fap2= float(_2fap2)
            # FAP30.00FAP3_
            _2fap3= float(_2fap3)
            # FV10.00FV1_
            _2fv1= float(_2fv1)
            # FV20.00FV2_
            _2fv2= float(_2fv2)
            # FV30.00FV3_
            _2fv3= float(_2fv3)
            # FTP0.00FTP
            _2ftp= float(_2ftp)* _2CTfactor
            
            if(math.isnan(_2ftrp)):
                _2ftrp=0
            if(math.isnan(_2frp1)):
                _2frp1=0
            if(math.isnan(_2frp2)):
                _2frp2=0
            if(math.isnan(_2frp3)):
                _2frp3=0
            if(math.isnan(_2ftap)):
                _2ftap=0
            if(math.isnan(_2fap1)):
                _2fap1=0
            if(math.isnan(_2fap2)):
                _2fap2=0
            if(math.isnan(_2fap3)):
                _2fap3=0
            if(math.isnan(_2fv1)):
                _2fv1=0
            if(math.isnan(_2fv2)):
                _2fv2=0
            if(math.isnan(_2fv3)):
                _2fv3=0
            if(math.isnan(_2ftp)):
                _2ftp=0

            
        except:
            print("2. Error occured while converting to string meter2a")  
            
            # FTRP0.00FTRP_
            _2ftrp= 0
            # FRP10.00FRP1_
            _2frp1=  0
            # FRP20.00FRP2_
            _2frp2=  0      
            # FRP30.00FRP3_
            _2frp3= 0
            # FTAP0.00FTAP_
            _2ftap= 0
            # FAP10.00FAP1_
            _2fap1= 0
            # FAP20.00FAP2_
            _2fap2= 0
            # FAP30.00FAP3_
            _2fap3= 0
            # FV10.00FV1_
            _2fv1= 0
            # FV20.00FV2_
            _2fv2= 0
            # FV30.00FV3_
            _2fv3= 0
            # FTP0.00FTP
            _2ftp= 0
            

    if msg.topic=="meter2b":
        meter2b = str(msg.payload, 'UTF-8') 
            
        print('meter2b Values: ' + meter2b)
      
        # FPFT0.70FPFT
        _2fpft= (meter2b[meter2b.find('FPFT')+4:meter2b.find('FPFT_')])
        _2te = (meter2b[meter2b.find('FFTE')+4:meter2b.find('FFTE_')])
        _2freq = (meter2b[meter2b.find('FFREQ')+5:meter2b.find('FFREQ_')])
        _2fp1 = (meter2b[meter2b.find('FP1')+3:meter2b.find('FP1_')])
        _2fp2 = (meter2b[meter2b.find('FP2')+3:meter2b.find('FP2_')])
        _2fp3 = (meter2b[meter2b.find('FP3')+3:meter2b.find('FP3_')])
        _2fct1 = (meter2b[meter2b.find('FCT1')+4:meter2b.find('FCT1_')])
        _2fct2 = (meter2b[meter2b.find('FCT2')+4:meter2b.find('FCT2_')])
        _2fct3 = (meter2b[meter2b.find('FCT3')+4:meter2b.find('FCT3_')])
        _2fpf1 = (meter2b[meter2b.find('FPF1')+4:meter2b.find('FPF1_')])
        _2fpf2 = (meter2b[meter2b.find('FPF2')+4:meter2b.find('FPF2_')])
        _2fpf3 = (meter2b[meter2b.find('FPF3')+4:meter2b.find('FPF3_')])
        _2ipaddress = meter2b[meter2b.find('IP')+2:meter2b.find('IP_')]
        _2meterid = meter2b[meter2b.find('MID')+3:meter2b.find('MID_')]
        # totalenergy = float(totalenergy)
        try:
            _2fpft = float(_2fpft)
            _2fp1 = float(_2fp1)*_2CTfactor
            _2fp2 = float(_2fp2)*_2CTfactor
            _2fp3 = float(_2fp3)*_2CTfactor
            _2fct1 = float(_2fct1)*_2CTfactor
            _2fct1 = round(_2fct1,2)
            _2fct2 = float(_2fct2)*_2CTfactor
            _2fct2 = round(_2fct2,2)
            _2fct3 = float(_2fct3)*_2CTfactor
            _2fct3 = round(_2fct3,2)
            _2fpf1 = float(_2fpf1)
            _2fpf2 = float(_2fpf2)
            _2fpf3 = float(_2fpf3)
            if(math.isnan(_2fpft)):
                _2fpft=0
            if(math.isnan(_2fp1)):
                _2fp1=0
            if(math.isnan(_2fp2)):
                _2fp2=0
            if(math.isnan(_2fp3)):
                _2fp3=0
            if(math.isnan(_2fct1)):
                _2fct1=0
            if(math.isnan(_2fct2)):
                _2fct2=0
            if(math.isnan(_2fct3)):
                _2fct3=0
            if(math.isnan(_2fpf1)):
                _2fpf1=0
            if(math.isnan(_2fpf2)):
                _2fpf2=0
            if(math.isnan(_2fpf3)):
                _2fpf3=0

            if(_2fpf1<0.1):
                _2fpf1=_2fpf1*10
            if(_2fpf2<0.1):
                _2fpf2=_2fpf2*10
            if(_2fpf3<0.1):
                _2fpf3=_2fpf3*10
            if(_2fpft<0.1):
                _2fpft=_2fpft*10
        except:
            print("2. Error occured while converting to string meter2b")
            _2fpft=0
            _2fp1 = 0
            _2fp2 = 0
            _2fp3 = 0
            _2fct1 = 0
            _2fct2 = 0
            _2fct3 = 0
            _2fpf1 = 0
            _2fpf2 = 0
            _2fpf3 = 0

        print('_2TE: ' + str(_2te))
        print('_2FREQ: ' + str(_2freq))
            # FV10.00FV1_
        print('_2FV1: '+str(_2fv1))
            # FV20.00FV2_
        print('_2FV2: '+str(_2fv2))
            # FV30.00FV3_
        print('_2FV3: '+str(_2fv3))
        print('_2FCT1: ' + str(_2fct1))
        print('_2FCT2: ' + str(_2fct2))
        print('_2FCT3: ' + str(_2fct3))
        print('_2FTP: '+str(_2ftp))
        print('_2FP1: ' + str(_2fp1))
        print('_2FP2: ' + str(_2fp2))
        print('_2FP3: ' + str(_2fp3))
        # FTRP0.00FTRP_
        print('_2FTRP: '+str(_2ftrp))
            # FRP10.00FRP1_
        print('_2FRP1: '+str(_2frp1))            
            # FRP20.00FRP2_
        print('_2FRP2: '+str(_2frp2))
            # FRP30.00FRP3_
        print('_2FRP3: '+str(_2frp3))
            # FTAP0.00FTAP_
        print('_2FTAP: '+str(_2ftap))
            # FAP10.00FAP1_
        print('_2FAP1: '+str(_2fap1))
            # FAP20.00FAP2_
        print('_2FAP2: '+str(_2fap2))
            # FAP30.00FAP3_
        print('_2FAP3: '+str(_2fap3))
        print('_2FPFT: '+str(_2fpft))
        print('_2FPF1: ' + str(_2fpf1))
        print('_2FPF2: ' + str(_2fpf2))
        print('_2FPF3: ' + str(_2fpf3))
        print('_2CT Factor:' +str(_2CTfactor))
        print('_2Ipaddress ' + _2ipaddress)
        print('_2Meter Id ' + _2meterid)

        

    if msg.topic=="meter4a":
        meter3a = str(msg.payload, 'UTF-8') 
        print('meter4a Values: ' + meter3a)
        # FTRP0.00FTRP_
        _3ftrp= (meter3a[meter3a.find('FTRP')+4:meter3a.find('FTRP_')])
        # FRP10.00FRP1_
        _3frp1= (meter3a[meter3a.find('FRP1')+4:meter3a.find('FRP1_')])
        # FRP20.00FRP2_
        _3frp2= (meter3a[meter3a.find('FRP2')+4:meter3a.find('FRP2_')])
        # FRP30.00FRP3_
        _3frp3= (meter3a[meter3a.find('FRP3')+4:meter3a.find('FRP3_')])
        # FTAP0.00FTAP_
        _3ftap= (meter3a[meter3a.find('FTAP')+4:meter3a.find('FTAP_')])
        # FAP10.00FAP1_
        _3fap1= (meter3a[meter3a.find('FAP1')+4:meter3a.find('FAP1_')])
        # FAP20.00FAP2_
        _3fap2= (meter3a[meter3a.find('FAP2')+4:meter3a.find('FAP2_')])
        # FAP30.00FAP3_
        _3fap3= (meter3a[meter3a.find('FAP3')+4:meter3a.find('FAP3_')])
        # FV10.00FV1_
        _3fv1= (meter3a[meter3a.find('FV1')+3:meter3a.find('FV1_')])
        # FV20.00FV2_
        _3fv2= (meter3a[meter3a.find('FV2')+3:meter3a.find('FV2_')])
        # FV30.00FV3_
        _3fv3= (meter3a[meter3a.find('FV3')+3:meter3a.find('FV3_')])
        # FTP0.00FTP
        _3ftp= (meter3a[meter3a.find('FTP')+3:meter3a.find('FTP_')])

        try:
            # FTRP0.00FTRP_
            _3ftrp= float(_3ftrp)
            # FRP10.00FRP1_
            _3frp1=  float(_3frp1)
            # FRP20.00FRP2_
            _3frp2=   float(_3frp2)       
            # FRP30.00FRP3_
            _3frp3= float(_3frp3)
            # FTAP0.00FTAP_
            _3ftap= float(_3ftap)
            _3ftap=_3ftap/1000
            # FAP10.00FAP1_
            _3fap1= float(_3fap1)
            # FAP20.00FAP2_
            _3fap2= float(_3fap2)
            # FAP30.00FAP3_
            _3fap3= float(_3fap3)
            # FV10.00FV1_
            _3fv1= float(_3fv1)
            # FV20.00FV2_
            _3fv2= float(_3fv2)
            # FV30.00FV3_
            _3fv3= float(_3fv3)
            # FTP0.00FTP
            _3ftp= float(_3ftp) * _3CTfactor
            if(math.isnan(_3ftrp)):
                _3ftrp=0
            if(math.isnan(_3frp1)):
                _3frp1=0
            if(math.isnan(_3frp2)):
                _3frp2=0
            if(math.isnan(_3frp3)):
                _3frp3=0
            if(math.isnan(_3ftap)):
                _3ftap=0
            if(math.isnan(_3fap1)):
                _3fap1=0
            if(math.isnan(_3fap2)):
                _3fap2=0
            if(math.isnan(_3fap3)):
                _3fap3=0
            if(math.isnan(_3fv1)):
                _3fv1=0
            if(math.isnan(_3fv2)):
                _3fv2=0
            if(math.isnan(_3fv3)):
                _3fv3=0
            if(math.isnan(_3ftp)):
                _3ftp=0

            
        except:
            print("2. Error occured while converting to string meter4a")  
            
            # FTRP0.00FTRP_
            _3ftrp= 0
            # FRP10.00FRP1_
            _3frp1=  0
            # FRP20.00FRP2_
            _3frp2=  0      
            # FRP30.00FRP3_
            _3frp3= 0
            # FTAP0.00FTAP_
            _3ftap= 0
            # FAP10.00FAP1_
            _3fap1= 0
            # FAP20.00FAP2_
            _3fap2= 0
            # FAP30.00FAP3_
            _3fap3= 0
            # FV10.00FV1_
            _3fv1= 0
            # FV20.00FV2_
            _3fv2= 0
            # FV30.00FV3_
            _3fv3= 0
            # FTP0.00FTP
            _3ftp= 0
            

    if msg.topic=="meter4b":
        meter3b = str(msg.payload, 'UTF-8') 
            
        print('meter4b Values: ' + meter3b)
      
        # FPFT0.70FPFT
        _3fpft= (meter3b[meter3b.find('FPFT')+4:meter3b.find('FPFT_')])
        _3tetemp = (meter3b[meter3b.find('FFTE')+4:meter3b.find('FFTE_')])
        _3freq = (meter3b[meter3b.find('FFREQ')+5:meter3b.find('FFREQ_')])
        _3fp1 = (meter3b[meter3b.find('FP1')+3:meter3b.find('FP1_')])
        _3fp2 = (meter3b[meter3b.find('FP2')+3:meter3b.find('FP2_')])
        _3fp3 = (meter3b[meter3b.find('FP3')+3:meter3b.find('FP3_')])
        _3fct1 = (meter3b[meter3b.find('FCT1')+4:meter3b.find('FCT1_')])
        _3fct2 = (meter3b[meter3b.find('FCT2')+4:meter3b.find('FCT2_')])
        _3fct3 = (meter3b[meter3b.find('FCT3')+4:meter3b.find('FCT3_')])
        _3fpf1 = (meter3b[meter3b.find('FPF1')+4:meter3b.find('FPF1_')])
        _3fpf2 = (meter3b[meter3b.find('FPF2')+4:meter3b.find('FPF2_')])
        _3fpf3 = (meter3b[meter3b.find('FPF3')+4:meter3b.find('FPF3_')])
        _3ipaddress = meter3b[meter3b.find('IP')+2:meter3b.find('IP_')]
        _3meterid = meter3b[meter3b.find('MID')+3:meter3b.find('MID_')]
        # totalenergy = float(totalenergy)
        try:
            _3fpft = float(_3fpft)
            if _3tetemp == '0.00':
                _3teArray.clear()
                _3teI=_3te
                print('Value reset')
            else:
                _3teArray.append(abs(float(_3tetemp)))
                _3te = _3teI + abs(_3teArray[-1] - _3teArray[0])
                
            _3freq = float(_3freq)
            _3fp1 = float(_3fp1)*_3CTfactor
            _3fp2 = float(_3fp2)*_3CTfactor
            _3fp3 = float(_3fp3)*_3CTfactor
            _3fct1 = float(_3fct1)*_3CTfactor
            _3fct1 = round(_3fct1,2)
            _3fct2 = float(_3fct2)*_3CTfactor
            _3fct2 = round(_3fct2,2)
            _3fct3 = float(_3fct3)*_3CTfactor
            _3fct3 = round(_3fct3,2)
            _3fpf1 = float(_3fpf1)
            _3fpf2 = float(_3fpf2)
            _3fpf3 = float(_3fpf3)
            _3fpf3 = round(_3fpf3,2)
            if(math.isnan(_3fpft) or _3fpft>5 or _3fpft<-5):
                _3fpft=0
            if(math.isnan(_3fp1)):
                _3fp1=0
            if(math.isnan(_3fp2)):
                _3fp2=0
            if(math.isnan(_3fp3)):
                _3fp3=0
            if(math.isnan(_3fct1)):
                _3fct1=0
            if(math.isnan(_3fct2)):
                _3fct2=0
            if(math.isnan(_3fct3)):
                _3fct3=0
            if(math.isnan(_3fpf1) or _3fpf1>5 or _3fpf1<-5):
                _3fpf1=0
            if(math.isnan(_3fpf2) or _3fpf2>5 or _3fpf2<-5):
                _3fpf2=0
            if(math.isnan(_3fpf3) or _3fpf3>5 or _3fpf3<-5):
                _3fpf3=0
            
            if(_3fpf1<0.1):
                _3fpf1=_3fpf1*10
            if(_3fpf2<0.1):
                _3fpf2=_3fpf2*10
            if(_3fpf3<0.1):
                _3fpf3=_3fpf3*10
            if(_3fpft<0.1):
                _3fpft=_3fpft*10
        except:
            print("2. Error occured while converting to string meter4b")
            _3fpft=0
            _3fp1 = 0
            _3fp2 = 0
            _3fp3 = 0
            _3fct1 = 0
            _3fct2 = 0
            _3fct3 = 0
            _3fpf1 = 0
            _3fpf2 = 0
            _3fpf3 = 0

        print('_3TE: ' + str(_3te))
        print(_3teArray)
        print(_3teI)
        
        print('_3FREQ: ' + str(_3freq))
            # FV10.00FV1_
        print('_3FV1: '+str(_3fv1))
            # FV20.00FV2_
        print('_3FV2: '+str(_3fv2))
            # FV30.00FV3_
        print('_3FV3: '+str(_3fv3))
        print('_3FCT1: ' + str(_3fct1))
        print('_3FCT2: ' + str(_3fct2))
        print('_3FCT3: ' + str(_3fct3))
        print('_3FTP: '+str(_3ftp))
        print('_3FP1: ' + str(_3fp1))
        print('_3FP2: ' + str(_3fp2))
        print('_3FP3: ' + str(_3fp3))
        # FTRP0.00FTRP_
        print('_3FTRP: '+str(_3ftrp))
            # FRP10.00FRP1_
        print('_3FRP1: '+str(_3frp1))            
            # FRP20.00FRP2_
        print('_3FRP2: '+str(_3frp2))
            # FRP30.00FRP3_
        print('_3FRP3: '+str(_3frp3))
            # FTAP0.00FTAP_
        print('_3FTAP: '+str(_3ftap))
            # FAP10.00FAP1_
        print('_3FAP1: '+str(_3fap1))
            # FAP20.00FAP2_
        print('_3FAP2: '+str(_3fap2))
            # FAP30.00FAP3_
        print('_3FAP3: '+str(_3fap3))
        print('_3FPFT: '+str(_3fpft))
        print('_3FPF1: ' + str(_3fpf1))
        print('_3FPF2: ' + str(_3fpf2))
        print('_3FPF3: ' + str(_3fpf3))
        print('_3CT Factor:' +str(_3CTfactor))
        print('_3Ipaddress ' + _3ipaddress)
        print('_3Meter Id ' + _3meterid)

try:
    client = mqtt.Client("digi_mqtt_test")  # Create instance of client with client ID “digi_mqtt_test”
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_message = on_message  # Define callback function for receipt of a message
    # client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
    client.username_pw_set(username="ali",password="verygood")
    client.connect('172.20.11.180')
    print('connected')
except:
    
    print('MQTT Server Error')

class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        global current_time
        global _1fpft
        global _1ftrp
        global _1frp1
        global _1frp2    
        global _1frp3
        global _1ftap
        global _1fap1
        global _1fap2
        global _1fap3
        global _1fv1
        global _1fv2
        global _1fv3
        global _1ftp
        global _1fpft
        global _1fp1
        global _1fpf1
        global _1fct1
        global _1fp2
        global _1fpf2
        global _1fct2
        global _1fp3
        global _1fpf3
        global _1fct3
        global _1te
        global _1freq
        global _1ftrp
        global _1meterid
        global _1fv1
        global _1fv2
        global _1fv3
        global _1rp1
        global _1rp2
        global _1rp3
        global _1tapr
        global _1rtapr
        global _1aap1r
        global _1aap2r
        global _1aap3r
        global _1trpr
        global _1tce
        global _1tcf
        global _1CTfactor
        
        while(1):
            client.loop()
            now = datetime.now(PST)
            secondscounter = now.strftime("%S")
            minutescounter = now.strftime("%M")
            current_time = now.strftime("%d/%m/%y-%H:%M:%S")
            _1frp3 = (_1fap3 * _1fap3) - (_1fp3*_1fp3)
            # _1frp3 = math.sqrt(_1frp3)
            _1frp3 = round(_1frp3,2)
            _1ftp = _1fp1 + _1fp2 + _1fp3
            
            if(minutescounter[1]=='0' and secondscounter=='00'):
                print('written in database ')
                conn = sqlite3.connect('customer.db')
                c=conn.cursor() 
                
                c.execute("SELECT rowid, * FROM consumption1V3")
                # 'datetime':current_time, 'te': _1te,'freq':_1freq,'fv1':_1fv1,'fv2':_1fv2,'fv3':_1fv3,'fct1':_1fct1,'fct2':_1fct2,'fct3':_1fct3,'ftp':_1ftp,'fp1':_1fp1,'fp2':_1fp2,'fp3':_1fp3,'ftrp':_1ftrp,'frp1':_1frp1,"frp2":_1frp2,'frp3':_1frp3,'ftap':_1ftap,'fap1':_1fap1,'fap2':_1fap2, 'fap3':_1fap3, 'fpft':_1fpft, 'fpf1':_1fpf1, 'fpf2': _1fpf2, 'fpf3': _1fpf3,'ipaddress':_1ipaddress ,'meterid':_1meterid
                c.execute("INSERT INTO consumption1V3 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (current_time, str(_1te), str(_1freq), str(_1fv1), str(_1fv2), str(_1fv3), str(_1fct1), str(_1fct2), str(_1fct3),str(_1ftp), str(_1fp1), str(_1fp2), str(_1fp3), str(_1ftrp), str(_1frp1), str(_1frp2), str(_1frp3), str(_1ftap), str(_1fap1), str(_1fap2), str(_1fap3), str(_1fpft), str(_1fpf1), str(_1fpf2), str(_1fpf3), str(_1meterid), str(_1CTfactor),'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil'))
                conn.commit()
                
                _1fpft=0
                _1ftrp= 0
                _1frp1=  0
                # FRP20.00FRP2_
                _1frp2=  0      
                # FRP30.00FRP3_
                _1frp3= 0
                # FTAP0.00FTAP_
                _1ftap= 0
                # FAP10.00FAP1_
                _1fap1= 0
                # FAP20.00FAP2_
                _1fap2= 0
                # FAP30.00FAP3_
                _1fap3= 0
                # FV10.00FV1_
                _1fv1= 0
                # FV20.00FV2_
                _1fv2= 0
                # FV30.00FV3_
                _1fv3= 0
                # FTP0.00FTP
                _1ftp= 0
                _1fp1=0
                _1fpf1=0
                _1fct1=0
                _1fp2=0
                _1fpf2=0
                _1fct2=0
                _1fp3=0
                _1fpf3=0
                _1fct3=0
                _1te=0
                _1freq=0
                _1meterid=0
                _1rp1=0
                _1rp2=0
                _1rp3=0
                _1tapr=0
                _1rtapr=0
                _1aap1r=0
                _1aap2r=0
                _1aap3r=0
                _1trpr=0
                _1tce=0
                _1tcf=0
             
            client.publish('time', current_time)
            client.publish('_1ftp', _1ftp)
            client.publish('_1fv1', _1fv1)
            client.publish('_1fv2', _1fv2)
            client.publish('_1fv3', _1fv3)
            client.publish('_1fct1', _1fct1)
            client.publish('_1fct2', _1fct2)
            client.publish('_1fct3', _1fct3)
            client.publish('_1fp1', _1fp1)
            client.publish('_1fp2', _1fp2)
            client.publish('_1fp3', _1fp3)
            
            
            await self.send(json.dumps({'datetime':current_time, 'te': _1te,'freq':_1freq,'fv1':_1fv1,'fv2':_1fv2,'fv3':_1fv3,'fct1':_1fct1,'fct2':_1fct2,'fct3':_1fct3,'ftp':_1ftp,'fp1':_1fp1,'fp2':_1fp2,'fp3':_1fp3,'ftrp':_1ftrp,'frp1':_1frp1,"frp2":_1frp2,'frp3':_1frp3,'ftap':_1ftap,'fap1':_1fap1,'fap2':_1fap2, 'fap3':_1fap3, 'fpft':_1fpft, 'fpf1':_1fpf1, 'fpf2': _1fpf2, 'fpf3': _1fpf3,'ipaddress':_1ipaddress ,'meterid':_1meterid, 'CTfactor':_1CTfactor}))
            await sleep(1)

class DashConsumer2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        global current_time
        global _2fpft
        global _2ftrp
        global _2frp1
        global _2frp2    
        global _2frp3
        global _2ftap
        global _2fap1
        global _2fap2
        global _2fap3
        global _2fv1
        global _2fv2
        global _2fv3
        global _2ftp
        global _2fpft
        global _2fp1
        global _2fpf1
        global _2fct1
        global _2fp2
        global _2fpf2
        global _2fct2
        global _2fp3
        global _2fpf3
        global _2fct3
        global _2te
        global _2freq
        global _2ftp
        global _2ftrp
        global _2meterid
        global _2fv1
        global _2fv2
        global _2fv3
        global _2rp1
        global _2rp2
        global _2rp3
        global _2tapr
        global _2rtapr
        global _2aap1r
        global _2aap2r
        global _2aap3r
        global _2trpr
        global _2tce
        global _2tcf
        global _2CTfactor
        
        while(1):
            client.loop()
            now = datetime.now(PST)
            secondscounter = now.strftime("%S")
            minutescounter = now.strftime("%M")
            current_time = now.strftime("%d/%m/%y-%H:%M:%S")
            if(minutescounter[1]=='0' and secondscounter=='00'):
                print('written in database ')
                conn = sqlite3.connect('customer.db')
                c=conn.cursor() 
                
                c.execute("SELECT rowid, * FROM consumption2V3")
                # 'datetime':current_time, 'te': _2te,'freq':_2freq,'fv1':_2fv1,'fv2':_2fv2,'fv3':_2fv3,'fct1':_2fct1,'fct2':_2fct2,'fct3':_2fct3,'ftp':_2ftp,'fp1':_2fp1,'fp2':_2fp2,'fp3':_2fp3,'ftrp':_2ftrp,'frp1':_2frp1,"frp2":_2frp2,'frp3':_2frp3,'ftap':_2ftap,'fap1':_2fap1,'fap2':_2fap2, 'fap3':_2fap3, 'fpft':_2fpft, 'fpf1':_2fpf1, 'fpf2': _2fpf2, 'fpf3': _2fpf3,'ipaddress':_2ipaddress ,'meterid':_2meterid
                c.execute("INSERT INTO consumption2V3 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (current_time, str(_2te), str(_2freq), str(_2fv1), str(_2fv2), str(_2fv3), str(_2fct1), str(_2fct2), str(_2fct3),str(_2ftp), str(_2fp1), str(_2fp2), str(_2fp3), str(_2ftrp), str(_2frp1), str(_2frp2), str(_2frp3), str(_2ftap), str(_2fap1), str(_2fap2), str(_2fap3), str(_2fpft), str(_2fpf1), str(_2fpf2), str(_2fpf3), str(_2meterid), str(_2CTfactor),'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil'))
                conn.commit()
                
                _2fpft=0
                _2ftrp= 0
                _2frp1=  0
                # FRP20.00FRP2_
                _2frp2=  0      
                # FRP30.00FRP3_
                _2frp3= 0
                # FTAP0.00FTAP_
                _2ftap= 0
                # FAP10.00FAP1_
                _2fap1= 0
                # FAP20.00FAP2_
                _2fap2= 0
                # FAP30.00FAP3_
                _2fap3= 0
                # FV10.00FV1_
                _2fv1= 0
                # FV20.00FV2_
                _2fv2= 0
                # FV30.00FV3_
                _2fv3= 0
                # FTP0.00FTP
                _2ftp= 0
                _2fp1=0
                _2fpf1=0
                _2fct1=0
                _2fp2=0
                _2fpf2=0
                _2fct2=0
                _2fp3=0
                _2fpf3=0
                _2fct3=0
                _2te=0
                _2freq=0
                _2meterid=0
                _2rp1=0
                _2rp2=0
                _2rp3=0
                _2tapr=0
                _2rtapr=0
                _2aap1r=0
                _2aap2r=0
                _2aap3r=0
                _2trpr=0
                _2tce=0
                _2tcf=0
             
            client.publish('time', current_time)
            # print(current_time)
            await self.send(json.dumps({'datetime':current_time, 'te': _2te,'freq':_2freq,'fv1':_2fv1,'fv2':_2fv2,'fv3':_2fv3,'fct1':_2fct1,'fct2':_2fct2,'fct3':_2fct3,'ftp':_2ftp,'fp1':_2fp1,'fp2':_2fp2,'fp3':_2fp3,'ftrp':_2ftrp,'frp1':_2frp1,"frp2":_2frp2,'frp3':_2frp3,'ftap':_2ftap,'fap1':_2fap1,'fap2':_2fap2, 'fap3':_2fap3, 'fpft':_2fpft, 'fpf1':_2fpf1, 'fpf2': _2fpf2, 'fpf3': _2fpf3,'ipaddress':_2ipaddress ,'meterid':_2meterid, 'CTfactor':_2CTfactor}))
            await sleep(1)

class DashConsumer3(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        global current_time
        global _3fpft
        global _3ftrp
        global _3frp1
        global _3frp2    
        global _3frp3
        global _3ftap
        global _3fap1
        global _3fap2
        global _3fap3
        global _3fv1
        global _3fv2
        global _3fv3
        global _3ftp
        global _3fpft
        global _3fp1
        global _3fpf1
        global _3fct1
        global _3fp2
        global _3fpf2
        global _3fct2
        global _3fp3
        global _3fpf3
        global _3fct3
        global _3te
        global _3freq
        global _3ftp
        global _3ftrp
        global _3meterid
        global _3fv1
        global _3fv2
        global _3fv3
        global _3rp1
        global _3rp2
        global _3rp3
        global _3tapr
        global _3rtapr
        global _3aap1r
        global _3aap2r
        global _3aap3r
        global _3trpr
        global _3tce
        global _3tcf
        global _3CTfactor
        global _3todayconsumption
        
        while(1):
            client.loop()
            now = datetime.now(PST)
            secondscounter = now.strftime("%S")
            minutescounter = now.strftime("%M")
            current_time = now.strftime("%d/%m/%y-%H:%M:%S")
            _3ftp = _3fp1+_3fp2+_3fp3
            if(minutescounter[1]=='0' and secondscounter=='00'):
                print('written in database ')
                conn = sqlite3.connect('customer.db')
                c=conn.cursor() 
                
                c.execute("SELECT rowid, * FROM consumption4V3")
                # 'datetime':current_time, 'te': _3te,'freq':_3freq,'fv1':_3fv1,'fv2':_3fv2,'fv3':_3fv3,'fct1':_3fct1,'fct2':_3fct2,'fct3':_3fct3,'ftp':_3ftp,'fp1':_3fp1,'fp2':_3fp2,'fp3':_3fp3,'ftrp':_3ftrp,'frp1':_3frp1,"frp2":_3frp2,'frp3':_3frp3,'ftap':_3ftap,'fap1':_3fap1,'fap2':_3fap2, 'fap3':_3fap3, 'fpft':_3fpft, 'fpf1':_3fpf1, 'fpf2': _3fpf2, 'fpf3': _3fpf3,'ipaddress':_3ipaddress ,'meterid':_3meterid
                c.execute("INSERT INTO consumption4V3 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (current_time, str(_3te), str(_3freq), str(_3fv1), str(_3fv2), str(_3fv3), str(_3fct1), str(_3fct2), str(_3fct3),str(_3ftp), str(_3fp1), str(_3fp2), str(_3fp3), str(_3ftrp), str(_3frp1), str(_3frp2), str(_3frp3), str(_3ftap), str(_3fap1), str(_3fap2), str(_3fap3), str(_3fpft), str(_3fpf1), str(_3fpf2), str(_3fpf3), str(_3meterid), str(_3CTfactor),str(_3todayconsumption), 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil'))
                conn.commit()
                
                _3fpft=0
                _3ftrp= 0
                _3frp1=  0
                # FRP20.00FRP2_
                _3frp2=  0      
                # FRP30.00FRP3_
                _3frp3= 0
                # FTAP0.00FTAP_
                _3ftap= 0
                # FAP10.00FAP1_
                _3fap1= 0
                # FAP20.00FAP2_
                _3fap2= 0
                # FAP30.00FAP3_
                _3fap3= 0
                # FV10.00FV1_
                _3fv1= 0
                # FV20.00FV2_
                _3fv2= 0
                # FV30.00FV3_
                _3fv3= 0
                # FTP0.00FTP
                _3ftp= 0
                _3fp1=0
                _3fpf1=0
                _3fct1=0
                _3fp2=0
                _3fpf2=0
                _3fct2=0
                _3fp3=0
                _3fpf3=0
                _3fct3=0
                _3freq=0
                _3meterid=0
                _3rp1=0
                _3rp2=0
                _3rp3=0
                _3tapr=0
                _3rtapr=0
                _3aap1r=0
                _3aap2r=0
                _3aap3r=0
                _3trpr=0
                _3tce=0
                _3tcf=0
             
            
            
            client.publish('time', current_time)
            # print(current_time)
            await self.send(json.dumps({'datetime':current_time, 'te': _3te,'freq':_3freq,'fv1':_3fv1,'fv2':_3fv2,'fv3':_3fv3,'fct1':_3fct1,'fct2':_3fct2,'fct3':_3fct3,'ftp':_3ftp,'fp1':_3fp1,'fp2':_3fp2,'fp3':_3fp3,'ftrp':_3ftrp,'frp1':_3frp1,"frp2":_3frp2,'frp3':_3frp3,'ftap':_3ftap,'fap1':_3fap1,'fap2':_3fap2, 'fap3':_3fap3, 'fpft':_3fpft, 'fpf1':_3fpf1, 'fpf2': _3fpf2, 'fpf3': _3fpf3,'ipaddress':_3ipaddress ,'meterid':_3meterid, 'CTfactor':_3CTfactor}))
            await sleep(1)

def updatevalues():
    
    global _1fpft
    global _1fv1
    global _1fv2
    global _1fv3
    global _1fp1
    global _1fpf1
    global _1fct1
    global _1fp2
    global _1fpf2
    global _1fct2
    global _1fp3
    global _1fpf3
    global _1fct3
    global _1te
    global _1freq
    global _1meterid
    global _1ipaddress
    global _1rp1
    global _1rp2
    global _1rp3
    global _1tapr
    global _1rtapr
    global _1aap1r
    global _1aap2r
    global _1aap3r
    global _1trpr
    global _1tce
    global _1tcf
    global _1CTfactor
    conn = sqlite3.connect('customer.db')
    c=conn.cursor()
    c.execute("SELECT rowid, * FROM consumption1V3")
    items = c.fetchall()
    plotdata = []
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    for i in items:
    
        plotdata[0].append(int(i[1][0:2])) #day
        plotdata[1].append(int(i[1][3:5])) #month 
        plotdata[2].append(int(i[1][6:8])) #year
        plotdata[3].append(int(i[1][9:11])) #hour
        try:
            plotdata[4].append(float(i[2])) #value
            plotdata[5].append(float(i[10])) #value
        except:
            plotdata[4].append(0.0) #value
            plotdata[5].append(0.0) #valu
            
        plotdata[6].append(int(i[1][12:14])) #minute
        
    
    while(1):
        client.loop()
        now = datetime.now(PST)
        current_time = now.strftime("%d/%m/%y-%H:%M:%S")
        
        client.publish('time', current_time)
        print(current_time)

        return current_time, _1te,_1freq,_1fv1,_1fv2,_1fv3,_1fct1,_1fct2,_1fct3,_1ftp,_1fp1,_1fp2,_1fp3,_1ftrp,_1frp1,_1frp2,_1frp3,_1ftap,_1fap1,_1fap2,_1fap3, _1fpft, _1fpf1, _1fpf2,_1fpf3,_1ipaddress ,_1meterid,_1CTfactor, plotdata
                
def updatevalues2():
    
    
    global _2fpft
    global _2fv1
    global _2fv2
    global _2fv3
    global _2fp1
    global _2fpf1
    global _2fct1
    global _2fp2
    global _2fpf2
    global _2fct2
    global _2fp3
    global _2fpf3
    global _2fct3
    global _2te
    global _2freq
    global _2meterid
    global _2ipaddress
    global _2rp1
    global _2rp2
    global _2rp3
    global _2tapr
    global _2rtapr
    global _2aap1r
    global _2aap2r
    global _2aap3r
    global _2trpr
    global _2tce
    global _2tcf
    global _2CTfactor
    conn = sqlite3.connect('customer.db')
    c=conn.cursor()
    c.execute("SELECT rowid, * FROM consumption2V3")
    items = c.fetchall()
    plotdata = []
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    for i in items:
    
        plotdata[0].append(int(i[1][0:2])) #day
        plotdata[1].append(int(i[1][3:5])) #month 
        plotdata[2].append(int(i[1][6:8])) #year
        plotdata[3].append(int(i[1][9:11])) #hour
        try:
            plotdata[4].append(float(i[2])) #value
            plotdata[5].append(float(i[10])) #value
        except:
            plotdata[4].append(0.0) #value
            plotdata[5].append(0.0) #valu
        plotdata[6].append(int(i[1][12:14])) #minute
        
    
    while(1):
        client.loop()
        now = datetime.now(PST)
        current_time = now.strftime("%d/%m/%y-%H:%M:%S")
        
        client.publish('time', current_time)
        print(current_time)

        return current_time, _2te,_2freq,_2fv1,_2fv2,_2fv3,_2fct1,_2fct2,_2fct3,_2ftp,_2fp1,_2fp2,_2fp3,_2ftrp,_2frp1,_2frp2,_2frp3,_2ftap,_2fap1,_2fap2,_2fap3, _2fpft, _2fpf1, _2fpf2,_2fpf3,_2ipaddress ,_2meterid,_2CTfactor, plotdata
                
def updatevalues3():
    global _3fpft
    global _3fv1
    global _3fv2
    global _3fv3
    global _3fp1
    global _3fpf1
    global _3fct1
    global _3fp2
    global _3fpf2
    global _3fct2
    global _3fp3
    global _3fpf3
    global _3fct3
    global _3te
    global _3freq
    global _3meterid
    global _3ipaddress
    global _3rp1
    global _3rp2
    global _3rp3
    global _3tapr
    global _3rtapr
    global _3aap1r
    global _3aap2r
    global _3aap3r
    global _3trpr
    global _3tce
    global _3tcf
    global _3CTfactor
    global _3todayconsumption
    conn = sqlite3.connect('customer.db')
    c=conn.cursor()
    c.execute("SELECT rowid, * FROM consumption4V3")
    items = c.fetchall()
    plotdata = []
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    plotdata.append([])
    for ind,i in enumerate(items):
        if ind==0:
            diff=0
        else:
            p = datetime(int(i[1][6:8]),int(i[1][3:5]),int(i[1][0:2]), int(i[1][9:11]),int(i[1][12:14]),00)
            # n = datetime(int(i[ind-1][1][6:8]),int(i[ind-1][1][3:5]),int(i[ind-1][1][0:2]), int(i[ind-1][1][9:11]),int(i[ind-1][1][12:14]),00)
            n=datetime(2020,2,3,0,0,0)
            # p=datetime(2019,4,5,6,8,8)
            diff = n-p
        # _3todayconsumption= _3todayconsumption + abs(float(i[10])) * diff
        print(diff)
        print(_3todayconsumption)
        plotdata[0].append(int(i[1][0:2])) #day
        plotdata[1].append(int(i[1][3:5])) #month 
        plotdata[2].append(int(i[1][6:8])) #year
        plotdata[3].append(int(i[1][9:11])) #hour
        try:
            plotdata[4].append(float(i[2])) #value
            plotdata[5].append(float(i[10])) #value
        except:
            plotdata[4].append(0.0) #value
            plotdata[5].append(0.0) #valu
        plotdata[6].append(int(i[1][12:14])) #minute
        
    
    while(1):
        client.loop()
        now = datetime.now(PST)
        current_time = now.strftime("%d/%m/%y-%H:%M:%S")
        
        client.publish('time', current_time)
        print(current_time)

        return current_time, _3te,_3freq,_3fv1,_3fv2,_3fv3,_3fct1,_3fct2,_3fct3,_3ftp,_3fp1,_3fp2,_3fp3,_3ftrp,_3frp1,_3frp2,_3frp3,_3ftap,_3fap1,_3fap2,_3fap3, _3fpft, _3fpf1, _3fpf2,_3fpf3,_3ipaddress ,_3meterid, _3CTfactor,plotdata
                

conn.close()
websocket_urlPattern = [
    path('ws/site1/', DashConsumer.as_asgi()),
    path('ws/site2/', DashConsumer2.as_asgi()),
    path('ws/site3/', DashConsumer3.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})


# document.querySelector('#TE').innerText =djangoData.te;
#                             document.querySelector('#FREQ').innerText =djangoData.freq;
#                             document.querySelector('#FV1').innerText =djangoData.fv1;
#                             document.querySelector('#FV2').innerText =djangoData.fv2;
#                             document.querySelector('#FV3').innerText =djangoData.fv3;
#                             document.querySelector('#FCT1').innerText =djangoData.fct1;
#                             document.querySelector('#FCT2').innerText =djangoData.fct2;
#                             document.querySelector('#FCT3').innerText =djangoData.fct3;
#                             document.querySelector('#FTP').innerText =djangoData.ftp;
#                             document.querySelector('#FP1').innerText =djangoData.fp1;
#                             document.querySelector('#FP2').innerText =djangoData.fp2;
#                             document.querySelector('#FP3').innerText =djangoData.fp3;
#                             document.querySelector('#FTRP').innerText =djangoData.ftrp;
#                             document.querySelector('#FRP1').innerText =djangoData.frp1;
#                             document.querySelector('#FRP2').innerText =djangoData.frp2;
#                             document.querySelector('#FRP3').innerText =djangoData.frp3;
#                             document.querySelector('#FTAP').innerText =djangoData.ftap;
#                             document.querySelector('#FAP1').innerText =djangoData.fap1;
#                             document.querySelector('#FAP2').innerText =djangoData.fap2;
#                             document.querySelector('#FAP3').innerText =djangoData.fap3;
#                             document.querySelector('#FPFT').innerText =djangoData.fpft;
#                             document.querySelector('#FPF1').innerText =djangoData.fpf1;
#                             document.querySelector('#FPF2').innerText =djangoData.fpf2;
#                             document.querySelector('#FPF3').innerText =djangoData.fpf3;
#                             document.querySelector('#ipaddress').innerText =djangoData.ipaddress;
#                             document.querySelector('#meterid').innerText =djangoData.meterid;