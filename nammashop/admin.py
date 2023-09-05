from django.contrib import admin
from .models import *

# Register your models here.

class change_display(admin.ModelAdmin):
    list_display = ('name','image','description')

admin.site.register(Category,change_display)
admin.site.register(Product)




