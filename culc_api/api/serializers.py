from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Schedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
        extra_kwargs = {
          'password': {'write_only': True},
          }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'nickName', 'subs', 'userSchedule')
        extra_kwargs = {'userSchedule': {'read_only': True}}
