from django.contrib import admin
from app.models import profile

# Register your models here.

@admin.register(profile)
class profileModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','dob','state','gender','location','pimage','rdoc']
