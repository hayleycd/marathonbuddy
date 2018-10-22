import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from twilio.rest import Client
from . import models
import random
import datetime

account_sid = os.environ['SID']
account_token = os.environ['AUTH_TOKEN'] 
my_phone = os.environ['PHONE_NUM']
twil_phone = os.environ['TWIL']

client = Client(account_sid, account_token)

def index(request):
	message = client.messages \
    	.create(
         body='Someone visited my site!',
         from_=twil_phone,
         to=my_phone,
     )
	return render(request, 'coaching/home.html', {})

def try_a_text(request):
	return render(request, 'coaching/try_a_text.html', {})

def send_text(request):
    compliments = models.Compliment.objects.all()
    your_message = compliments[random.randrange(0, len(compliments))].compliment
    message = client.messages \
    	.create(
         body=your_message,
         from_=twil_phone,
         to="+"+request.GET.get("phone_number"),
     )
    return redirect('/')

def who_are_you(request):
	return render(request, 'coaching/who_are_you.html')

def what_is_this(request):
	return render(request, 'coaching/what_is_this.html')

def upcoming_races(request):
    races = models.RunEvent.objects.filter(event_date__gte=datetime.datetime.now())
	return render(request, 'coaching/upcoming_races.html', {"races": races})