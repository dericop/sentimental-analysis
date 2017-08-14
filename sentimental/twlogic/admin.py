from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Twacount)
class TwacountAdmin(admin.ModelAdmin):
    list_display = ('acount', 'location',)
    list_filter = ['location']


@admin.register(Twcomment)
class TwcomentAdmin(admin.ModelAdmin):
    list_display = ('acount', 'comment', 'query')
    list_filter = ['query']
