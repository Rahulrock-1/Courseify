from rest_framework import serializers
from Course.models import course

class CouserSerializer(serializers.Model):
    
    class Meta:
        model = Course
        
        field = '__all__'
