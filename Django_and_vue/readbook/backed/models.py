from django.db import models
from account.models import *

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Collections(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(Account,related_name='collections',on_delete=models.CASCADE)

    def __str__(self):
        return '%d: %s' % (self.id,self.name)

class Books(models.Model):
    title = models.CharField(max_length=128)
    authors = models.CharField(max_length=256)
    publisher = models.CharField(max_length=128)
    # publish_date = models.DateField()
    categories = models.CharField(max_length=128)
    collection = models.ForeignKey(Collections,related_name='books',on_delete=models.CASCADE)

    def __str__(self):
      return self.title


# 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
