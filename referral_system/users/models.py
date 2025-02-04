from django.db import models
import uuid

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    referral_code = models.CharField(max_length=10, unique=True, default=str(uuid.uuid4())[:8])
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')

    def __str__(self):
        return self.name
