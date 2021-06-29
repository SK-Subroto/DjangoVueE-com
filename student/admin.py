from django.contrib import admin
from .models import Studentmodel, Markmodel

# Register your models here.
admin.site.register(Studentmodel)
admin.site.register(Markmodel)