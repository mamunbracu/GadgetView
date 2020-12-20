from django.db import models
from django.conf import settings

# Create your models here.
class UserComplain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_code = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, null=False)
    your_complain = models.TextField(max_length=300, blank=True)

    def __str__(self):
         return f'{self.user.profile.username} Complain'

