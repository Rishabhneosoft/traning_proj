from django.contrib import admin

# Register your models here.
from .models import *

# Register your models h
admin.site.register(User)
admin.site.register(Assignment)
admin.site.register(Review)
admin.site.register(Traning)
admin.site.register(Client)