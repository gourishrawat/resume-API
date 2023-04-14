from pyexpat import model
from rest_framework import serializers
from app.models import profile

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields=['id','name','email','dob','state','gender','location','pimage','rdoc']