from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    bio = models.TextField()

    class Meta:
        db_name = 'sellers'
        verbos_name = 'Продавец'
        verbos_name_plural = 'Продавцы'
