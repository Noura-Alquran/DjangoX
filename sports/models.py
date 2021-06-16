from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Sport(models.Model):
    player_name = models.CharField(max_length=64)
    coach_s_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="")

    def get_absolute_url(self):
        return reverse('sport_detail', args=[str(self.id)])

    def __str__(self):
        return self.player_name
