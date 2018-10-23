from django.contrib import admin
from .models import Cheer, RunUpdate, RunEvent, Picture, Compliment, Visitor

admin.site.register(Cheer)
admin.site.register(RunUpdate)
admin.site.register(RunEvent)
admin.site.register(Picture)
admin.site.register(Compliment)
admin.site.register(Visitor)