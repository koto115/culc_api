from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
import uuid
from django.db.models.deletion import CASCADE
from django.db.models.fields import UUIDField

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('username need to be set')

        user = self.model(username=self.model.normalize_username(username))
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100, unique=True, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)

  USERNAME_FIELD = 'username'

  objects = UserManager()

  def __str__(self):
      return self.username

# uuidのハイフンをなくすfield
class MyUUIDField(UUIDField):
  def prepare_value(self, value):
    if isinstance(value, uuid.UUID):
      return value.hex
    return value

class Schedule(models.Model):
  id = MyUUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  nickName = models.CharField(max_length=100)
  userSchedule = models.ForeignKey(
    settings.AUTH_USER_MODEL, related_name='userSchedule',
    on_delete=models.CASCADE
  )

  subs = ArrayField(models.CharField(max_length=100, blank=True, null=True, default=''), blank=True, null=True, size=29)

  def __str__(self):
    return self.nickName