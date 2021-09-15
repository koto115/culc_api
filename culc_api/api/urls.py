from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

# URLの末尾にid番号を入れられる
router = DefaultRouter()
router.register('schedule', views.SchedulesView),

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('myschedule/', views.MyScheduleView.as_view(), name='myschedule'),
    path('', include(router.urls)),
]