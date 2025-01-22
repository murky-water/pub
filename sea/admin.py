from django.contrib import admin
from .models import *
# Register your models here.
myModels = [Hour,City,Address,Hotel]
admin.site.register(myModels)

