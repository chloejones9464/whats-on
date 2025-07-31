from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=10,
        choices=[
            ('public', 'Public'),
            ('bar', 'Bar Owner')
        ],
        default='public'
    )
    bar_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
