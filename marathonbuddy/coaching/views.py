import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from twilio.rest import Client
from . import models
import random
import datetime
import time
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse

account_sid = os.environ['SID']
account_token = os.environ['AUTH_TOKEN'] 
my_phone = os.environ['PHONE_NUM']
twil_phone = os.environ['TWIL']

client = Client(account_sid, account_token)

def index(request):
    updates = models.RunUpdate.objects.all().order_by('-time_stamp')
    num_updates = len(updates) if len(updates) < 5 else 5
    rendered_updates = updates[0 : num_updates]
    return render(request, 'coaching/home.html', {'updates' : rendered_updates})

def try_a_text(request):
	return render(request, 'coaching/try_a_text.html', {})

def send_text(request):
    nickname = request.GET.get('nickname')
    how = request.GET.get('how')

    if nickname and how:
        models.Visitor(nickname=nickname, how=how).save()

    compliments = models.Compliment.objects.all()
    your_message = compliments[random.randrange(0, len(compliments))].compliment + \
        "\nThanks for dropping by! Feel free to see my work at www.codeandtea.com"
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

def races(request):
    now = datetime.datetime.now()
    upcoming_races = models.RunEvent.objects.filter(event_date__gte=now)
    past_races = models.RunEvent.objects.filter(event_date__lte=now)
	return render(request, 'coaching/upcoming_races.html', {"races": upcoming_races, "past": past_races})

@csrf_exempt
def sms_interaction(request, methods=['GET', 'POST']):

    body = request.POST.get('Body', None)
    message_sid = request.POST.get('MessageSid', None)
    
    #This allows me to send short updates from my phone.

    if request.POST.get('From') == my_phone:
        if body[0] == "#":
            models.RunUpdate(text_body=body[1:], time_stamp=datetime.datetime.now()).save()

    cheers = [cheer.text_body for cheer in models.Cheer.objects.all()]
    random.shuffle(cheers)

    your_message = cheers[0]
    resp = MessagingResponse()
    resp.message(your_message)

    return HttpResponse(resp)

def add_cheer(request):
    cheer = request.GET.get('cheer')
    cheerleader = request.GET.get('cheerleader')

    if cheer:
        models.Cheer(text_body=cheer, cheerleader=cheerleader).save()

    return redirect('/')

def get_pictures(request):

    pass


