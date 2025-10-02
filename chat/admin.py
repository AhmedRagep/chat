from django.contrib import admin
from .models import *
# Register your models here.

class chatAdmin(admin.ModelAdmin):
  list_display = [
    'body',
    'sender',
    'reciever',
    'created_date',
  ]

admin.site.register([Profile,Frind])
admin.site.register(ChatMessage,chatAdmin)

