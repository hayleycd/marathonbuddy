import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from twilio.rest import Client
from . import models
import random
import datetime
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse

account_sid = os.environ['SID']
account_token = os.environ['AUTH_TOKEN'] 
my_phone = os.environ['PHONE_NUM']
twil_phone = os.environ['TWIL']

client = Client(account_sid, account_token)

def index(request):
	return render(request, 'coaching/home.html', {})

def try_a_text(request):
	return render(request, 'coaching/try_a_text.html', {})

def send_text(request):
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
    cheers = [cheer.text_body for cheer in models.Cheer.objects.all()]
    random.shuffle(cheers)

    if body.upper() == "INSPO":
        your_message = cheers[0]
        resp = MessagingResponse()
        resp.message(your_message)
        return HttpResponse(resp)

    elif body.upper() == "RACE":
        resp = MessagingResponse()

        for cheer in cheers:
            resp.message(cheer)

    else:
        your_message = "I'm sorry, I don't recognize the command."
        resp = MessagingResponse()
        resp.message(your_message)

    return HttpResponse(resp)
