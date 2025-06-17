from django.contrib.auth.models import AbstractUser
from django.db import models
from random import randint
class User(AbstractUser):
    phone=models.IntegerField(default=0)
    address=models.TextField(default="")
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=20, null=True, blank=True)
    role=models.CharField(default="")





    def generate_otp(self):
        otp_number=str(randint(1000,9999))+str(self.id)
        self.otp=otp_number
        self.save()