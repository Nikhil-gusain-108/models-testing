from django.contrib import admin
from .models import quiz,quiz_data,quiz_history,Quiz_types,options,Q_name
# Register your models here.

admin.site.register(Q_name)
admin.site.register(quiz)
admin.site.register(quiz_data)
admin.site.register(quiz_history)
admin.site.register(Quiz_types)
admin.site.register(options)