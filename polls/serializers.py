from rest_framework import serializers
from .models import task

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ('id','status_task' , 'complete')