from django.contrib import admin
from .models import reviews, user_details,reply
# Register your models here.

admin.site.register(reviews)
admin.site.register(user_details)
admin.site.register(reply)