from django.contrib import admin
from testapp.models import Login

class adminform(admin.ModelAdmin):
    list_display=('firstname','lastname','email')

admin.site.register(Login,adminform)