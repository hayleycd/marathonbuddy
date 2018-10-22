from django.db import models
from django.utils import timezone

class Cheer(models.Model):
	text_body = models.CharField(max_length=240)
	cheerleader = models.CharField(max_length=60)
	sent = models.BooleanField()
	time_stamp = models.DateTimeField()
	event = models.ForeignKey('RunEvent', null=True, on_delete=models.SET_NULL)


class RunUpdate(models.Model):
	text_body = models.CharField(max_length=240)
	time_stamp = models.DateTimeField()
	event = models.ForeignKey('RunEvent', null=True, on_delete=models.SET_NULL)


class RunEvent(models.Model):
	event_name = models.CharField(max_length=60)
	event_date = models.DateTimeField(null=True)
	distance = models.FloatField(null=True)
	goal_time = models.IntegerField(null=True)
	cutoff_time = models.IntegerField(null=True)
	city = models.CharField(max_length=60, blank=True)
	state = models.CharField(max_length=2, blank=True)
	start_time = models.DateTimeField(blank=True)
	stop_time = models.DateTimeField(blank=True)
	picture = models.ForeignKey('Picture', null=True, blank=True, on_delete=models.SET_NULL)


class Coaching(models.Model):
	text_body = models.CharField(max_length=240)
	previous_coaching_step = models.IntegerField(blank=True)
	run_event = models.ForeignKey('RunEvent', on_delete=models.SET_NULL, null=True)


class Picture(models.Model):
	description = models.CharField(max_length=240)
	url = models.CharField(max_length=500)

class Compliment(models.Model):
	compliment = models.CharField(max_length=140)
