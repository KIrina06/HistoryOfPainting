from django.contrib import admin

from .models import Status, Expertise, Application, User, ExpApp

admin.site.register(User)
admin.site.register(Status)
admin.site.register(Expertise)
admin.site.register(Application)
admin.site.register(ExpApp)