from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ordertrack import choices as c


class ProfileEdit(models.Model):
    displayPicture = models.ImageField(upload_to='dp')
    hallName = models.CharField(max_length=1055, choices=c.CHOICES_HallName)
    roomNumber = models.CharField(max_length=3)
    contact1 = models.CharField(max_length=11)
    contact2 = models.CharField(max_length=11, null=True, blank=True)
    profileAuthor = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profileAuthor.username

    def get_absolute_url_profile(self):
        return reverse('profile_views', kwargs={'username': self.profileAuthor.username})
