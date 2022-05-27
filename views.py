from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
from .forms import CreatenewList, CreateUserFormm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import paho.mqtt.client as mqtt
from random import randrange, uniform
import paho.mqtt.subscribe as subscribe
from django.contrib.auth.decorators import login_required
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

from .routing import updatevalues, updatevalues2, updatevalues3
# from .routing import updatevalues

import csv
import sqlite3



@login_required(login_url='login')
def home(response):
    context = {
        
    }
    return render(response, "main/home.html", context)


@login_required(login_url='login')
def site1(response):
    
    current_time, te,freq,fv1,fv2,fv3,fct1,fct2,fct3,ftp,fp1,fp2,fp3,ftrp,frp1,frp2,frp3,ftap,fap1,fap2,fap3, fpft, fpf1, fpf2,fpf3,ipaddress ,meterid, CTfactor,plotdata=updatevalues()
    status='off'
    if(fv1!=0):
        status='on'
    plotdatajson = json.dumps(plotdata)
    context = {
        'TE':te,
        'FREQ':freq,
        'FV1':fv1,
        'FV2':fv2,
        'FV3':fv3,
        'FCT1':fct1,
        'FCT2':fct2,
        'FCT3':fct3,
        'FTP':ftp,
        'FP1':fp1,
        'FP2':fp2,
        'FP3':fp3,
        'FTRP':ftrp,
        'FRP1':frp1,
        'FRP2':frp2,
        'FRP3':frp3,
        'FTAP':ftap,
        'FAP1':fap1,
        'FAP2':fap2,
        'FAP3':fap3, 
        'FPFT':fpft, 
        'FPF1':fpf1, 
        'FPF2':fpf2,
        'FPF3':fpf3,
        'status':status,
        "currentTime":current_time,
        "meterid":meterid,
        "ipaddress": ipaddress,
        'plotdatajson': plotdatajson,
        'CTfactor':CTfactor,
        # "power1": "power1",                
        # "phase1":"phase1",
        # "current1":"current1",
        # "power2":"power2",
        # "phase2":"phase2",
        # "current2":"current2",
        # "power3":"power3",
        # "phase3":"phase3",
        # "current3":"current3",
        # "totalenergy":"totalenergy",
        # "pehlipowervalue":"pehlipowervalue",
        # "frequency":"frequency",
    }
    return render(response, "main/site1.html", context)

@login_required(login_url='login')
def site1m(response):
    
    current_time, te,freq,fv1,fv2,fv3,fct1,fct2,fct3,ftp,fp1,fp2,fp3,ftrp,frp1,frp2,frp3,ftap,fap1,fap2,fap3, fpft, fpf1, fpf2,fpf3,ipaddress ,meterid, CTfactor,plotdata=updatevalues()
    
    plotdatajson = json.dumps(plotdata)
    context = {
        'TE':te,
        'FREQ':freq,
        'FV1':fv1,
        'FV2':fv2,
        'FV3':fv3,
        'FCT1':fct1,
        'FCT2':fct2,
        'FCT3':fct3,
        'FTP':ftp,
        'FP1':fp1,
        'FP2':fp2,
        'FP3':fp3,
        'FTRP':ftrp,
        'FRP1':frp1,
        'FRP2':frp2,
        'FRP3':frp3,
        'FTAP':ftap,
        'FAP1':fap1,
        'FAP2':fap2,
        'FAP3':fap3, 
        'FPFT':fpft, 
        'FPF1':fpf1, 
        'FPF2':fpf2,
        'FPF3':fpf3,
        'CTfactor':CTfactor,
        "currentTime":current_time,
        "meterid":meterid,
        "ipaddress": ipaddress,
        'plotdatajson': plotdatajson,
        # "power1": "power1",                
        # "phase1":"phase1",
        # "current1":"current1",
        # "power2":"power2",
        # "phase2":"phase2",
        # "current2":"current2",
        # "power3":"power3",
        # "phase3":"phase3",
        # "current3":"current3",
        # "totalenergy":"totalenergy",
        # "pehlipowervalue":"pehlipowervalue",
        # "frequency":"frequency",
    }
    return render(response, "main/site1m.html", context)


@login_required(login_url='login')
def site2(response):
    
    current_time, te,freq,fv1,fv2,fv3,fct1,fct2,fct3,ftp,fp1,fp2,fp3,ftrp,frp1,frp2,frp3,ftap,fap1,fap2,fap3, fpft, fpf1, fpf2,fpf3,ipaddress ,meterid, CTfactor,plotdata=updatevalues2()
    status='off'
    if(fv1!=0):
        status='on'
    plotdatajson = json.dumps(plotdata)
    context = {
        'TE':te,
        'FREQ':freq,
        'FV1':fv1,
        'FV2':fv2,
        'FV3':fv3,
        'FCT1':fct1,
        'FCT2':fct2,
        'FCT3':fct3,
        'FTP':ftp,
        'FP1':fp1,
        'FP2':fp2,
        'FP3':fp3,
        'FTRP':ftrp,
        'FRP1':frp1,
        'FRP2':frp2,
        'FRP3':frp3,
        'FTAP':ftap,
        'FAP1':fap1,
        'FAP2':fap2,
        'FAP3':fap3, 
        'FPFT':fpft, 
        'FPF1':fpf1, 
        'FPF2':fpf2,
        'FPF3':fpf3,
        'status':status,
        'CTfactor':CTfactor,
        "currentTime":current_time,
        "meterid":meterid,
        "ipaddress": ipaddress,
        'plotdatajson': plotdatajson,
        # "power1": "power1",                
        # "phase1":"phase1",
        # "current1":"current1",
        # "power2":"power2",
        # "phase2":"phase2",
        # "current2":"current2",
        # "power3":"power3",
        # "phase3":"phase3",
        # "current3":"current3",
        # "totalenergy":"totalenergy",
        # "pehlipowervalue":"pehlipowervalue",
        # "frequency":"frequency",
    }
    return render(response, "main/site2.html", context)


@login_required(login_url='login')
def site2m(response):
    
    current_time, te,freq,fv1,fv2,fv3,fct1,fct2,fct3,ftp,fp1,fp2,fp3,ftrp,frp1,frp2,frp3,ftap,fap1,fap2,fap3, fpft, fpf1, fpf2,fpf3,ipaddress ,meterid, CTfactor,plotdata=updatevalues2()
    
    plotdatajson = json.dumps(plotdata)
    context = {
        'TE':te,
        'FREQ':freq,
        'FV1':fv1,
        'FV2':fv2,
        'FV3':fv3,
        'FCT1':fct1,
        'FCT2':fct2,
        'FCT3':fct3,
        'FTP':ftp,
        'FP1':fp1,
        'FP2':fp2,
        'FP3':fp3,
        'FTRP':ftrp,
        'FRP1':frp1,
        'FRP2':frp2,
        'FRP3':frp3,
        'FTAP':ftap,
        'FAP1':fap1,
        'FAP2':fap2,
        'FAP3':fap3, 
        'FPFT':fpft, 
        'FPF1':fpf1, 
        'FPF2':fpf2,
        'FPF3':fpf3,
        'CTfactor':CTfactor,
        "currentTime":current_time,
        "meterid":meterid,
        "ipaddress": ipaddress,
        'plotdatajson': plotdatajson,
        # "power1": "power1",                
        # "phase1":"phase1",
        # "current1":"current1",
        # "power2":"power2",
        # "phase2":"phase2",
        # "current2":"current2",
        # "power3":"power3",
        # "phase3":"phase3",
        # "current3":"current3",
        # "totalenergy":"totalenergy",
        # "pehlipowervalue":"pehlipowervalue",
        # "frequency":"frequency",
    }
    return render(response, "main/site2m.html", context)

@login_required(login_url='login')
def site3(response):
    
    current_time, te,freq,fv1,fv2,fv3,fct1,fct2,fct3,ftp,fp1,fp2,fp3,ftrp,frp1,frp2,frp3,ftap,fap1,fap2,fap3, fpft, fpf1, fpf2,fpf3,ipaddress ,meterid, CTfactor,plotdata=updatevalues3()
    status='off'
    if(fv1!=0):
        status='on'
    plotdatajson = json.dumps(plotdata)
    context = {
        'TE':te,
        'FREQ':freq,
        'FV1':fv1,
        'FV2':fv2,
        'FV3':fv3,
        'FCT1':fct1,
        'FCT2':fct2,
        'FCT3':fct3,
        'FTP':ftp,
        'FP1':fp1,
        'FP2':fp2,
        'FP3':fp3,
        'FTRP':ftrp,
        'FRP1':frp1,
        'FRP2':frp2,
        'FRP3':frp3,
        'FTAP':ftap,
        'FAP1':fap1,
        'FAP2':fap2,
        'FAP3':fap3, 
        'FPFT':fpft, 
        'FPF1':fpf1, 
        'FPF2':fpf2,
        'FPF3':fpf3,
        'status':status,
        'CTfactor':CTfactor,
        "currentTime":current_time,
        "meterid":meterid,
        "ipaddress": ipaddress,
        'plotdatajson': plotdatajson,
        # "power1": "power1",                
        # "phase1":"phase1",
        # "current1":"current1",
        # "power2":"power2",
        # "phase2":"phase2",
        # "current2":"current2",
        # "power3":"power3",
        # "phase3":"phase3",
        # "current3":"current3",
        # "totalenergy":"totalenergy",
        # "pehlipowervalue":"pehlipowervalue",
        # "frequency":"frequency",
    }
    return render(response, "main/site3.html", context)

@login_required(login_url='login')
def download_file2(request):

    conn = sqlite3.connect('customer.db')
    # create a cursor
    c=conn.cursor()
    c.execute("SELECT rowid, * FROM consumption2V3")
    items = c.fetchall()
    with open('EMV002Data.csv','w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["No","Time",'te','freq','fv1','fv2','fv3','fct1','fct2','fct3','ftp','fp1','fp2','fp3','ftrp','frp1',"frp2",'frp3','ftap','fap1','fap2', 'fap3', 'fpft', 'fpf1', 'fpf2', 'fpf3','ipaddress','meterid'])
        for i in items:
            thewriter.writerow(i)

    print('File created')
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'EMV002Data.csv'
    # Define the full file path
    filepath = BASE_DIR +'/'+ filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

@login_required(login_url='login')
def download_file3(request):

    conn = sqlite3.connect('customer.db')
    # create a cursor
    c=conn.cursor()
    c.execute("SELECT rowid, * FROM consumption4V3")
    items = c.fetchall()
    with open('EMV003Data.csv','w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["No","Time",'te','freq','fv1','fv2','fv3','fct1','fct2','fct3','ftp','fp1','fp2','fp3','ftrp','frp1',"frp2",'frp3','ftap','fap1','fap2', 'fap3', 'fpft', 'fpf1', 'fpf2', 'fpf3','ipaddress','meterid'])
        for i in items:
            thewriter.writerow(i)

    print('File created')
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'EMV003Data.csv'
    # Define the full file path
    filepath = BASE_DIR +'/'+ filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


@login_required(login_url='login')   
def view(response):
    return render(response, "main/view.html", {})

@login_required(login_url='login')
def sensors(response):
    return render(response, "main/sensors.html", {})


@login_required(login_url='login')
def valuess(response):
    return render(response, "main/valuess.html", {})


def registerpage(response):
    if response.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserFormm()
        if response.method == "POST":
            form = UserCreationForm(response.POST)

            if form.is_valid():
                form.save()
                user =form.cleaned_data.get('username')
                messages.success(response, 'Account creatd for ' + user)
                return redirect('login')

        else: 
            form = CreateUserFormm()

        context = {'form':form}
        return render(response, "main/registerpage.html", context)


def loginpage(response):
    if response.user.is_authenticated:
        return redirect('home')
    else:
        if response.method == "POST":
            username=response.POST.get('username')
            password=response.POST.get('password')
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                return redirect('home')
            else:
                messages.info(response, 'Username or Password is incorrect')

        return render(response, "main/loginpage.html", {})

def logoutuser(request):
    logout(request)
    return redirect('login')
