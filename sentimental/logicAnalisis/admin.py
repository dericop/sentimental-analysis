from django.contrib import admin
from .models import *


class wordAdmin(admin.ModelAdmin):
    list_display = ('name', 'polarity', 'gram_root',)
    list_filter = ['polarity']


class user_facebookAdmin(admin.ModelAdmin):
    list_display = ('id_user','email','about_me', 'birthday', 'city', 'country', 'sex', 'religion',)
    list_filter = ['sex', 'religion']


class commentsClassifiedAdmin(admin.ModelAdmin):
    list_display = ('from_message_id', 'auto_classification', 'user_classification',)
    list_filter = ['id_page']

admin.site.register(user_facebook, user_facebookAdmin)
admin.site.register(page)
admin.site.register(message)
admin.site.register(interest)
admin.site.register(word, wordAdmin)
admin.site.register(polarity)
admin.site.register(commentsClassified, commentsClassifiedAdmin)




# Register your models here.
