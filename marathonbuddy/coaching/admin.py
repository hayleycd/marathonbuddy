from django.contrib import admin
from .models import Cheer, RunUpdate, RunEvent, Picture, Compliment, Visitor

class CheerAdmin(admin.ModelAdmin):
	list_display = ('text_body', 'cheerleader',)


class RunUpdateAdmin(admin.ModelAdmin):
	list_display = ('text_body', 'time_stamp',)


class RunEventAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'event_date',)


class PictureAdmin(admin.ModelAdmin):
	list_display = ('description',)


class ComplimentAdmin(admin.ModelAdmin):
	list_display = ('Compliment',)


class VisitorAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'how',)
admin.site.register(Cheer, CheerAdmin)
admin.site.register(RunUpdate, RunUpdateAdmin)
admin.site.register(RunEvent, RunEventAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Compliment, ComplimentAdmin)
admin.site.register(Visitor)