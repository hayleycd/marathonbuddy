from django.db import models
from django.utils import timezone

class Cheer(models.Model):
	text_body = models.TextField()
	cheerleader = models.CharField(max_length=60)


class RunUpdate(models.Model):
	text_body = models.CharField(max_length=240)
	time_stamp = models.DateTimeField()


class RunEvent(models.Model):
	event_name = models.CharField(max_length=60)
	event_date = models.DateTimeField(null=True)
	distance = models.FloatField(null=True)
	city = models.CharField(max_length=60, blank=True)
	state = models.CharField(max_length=2, blank=True)
	picture = models.ForeignKey('Picture', null=True, blank=True, on_delete=models.SET_NULL)
	summary = models.TextField(null=True)


class Picture(models.Model):
	description = models.CharField(max_length=240)
	url = models.CharField(max_length=500)


class Compliment(models.Model):
	compliment = models.CharField(max_length=140)


class Visitor(models.Model):
	nickname = models.CharField(max_length=140)
	how = models.TextField(null=True)
