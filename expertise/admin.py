from django.contrib import admin

from expertise.models import User, Status, Expertise, Application, ExpApp

admin.site.register(User)
admin.site.register(Status)
admin.site.register(Expertise)
admin.site.register(Application)
admin.site.register(ExpApp)