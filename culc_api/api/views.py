from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Schedule


class CreateUserView(generics.CreateAPIView):
  serializer_class = serializers.UserSerializer
  permission_classes = (AllowAny,)

class SchedulesView(viewsets.ModelViewSet):
  queryset = Schedule.objects.all()
  serializer_class = serializers.ScheduleSerializer

  def perform_create(self, serializer):
    serializer.save(userSchedule=self.request.user)

# 上でscheduleを作ってmyscheduleで検索して持ってくる
class MyScheduleView(generics.ListAPIView):
  queryset = Schedule.objects.all()
  serializer_class = serializers.ScheduleSerializer

  def get_queryset(self):
    return self.queryset.filter(userSchedule=self.request.user)