from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from userprofile.models import ProfileEdit
from ordertrack import choices as c


class PostOrderRequest(models.Model):
    author = models.ForeignKey(ProfileEdit, on_delete=models.CASCADE)
    pickupPointType = models.CharField(max_length=50, choices=c.CHOICES_PickupPointType)
    pickupPoint = models.CharField(max_length=105, choices=c.CHOICES_PickupPoint)
    pickupPointDescription = models.CharField(max_length=2055)
    deliveryPoint = models.CharField(max_length=255, choices=c.CHOICES_HallName)
    parcelType = models.CharField(max_length=255, choices=c.CHOICES_ParcelType)
    parcelDescription = models.CharField(max_length=2055)
    weight = models.DecimalField(decimal_places=2, max_digits=4)
    deliveryDate = models.DateField(help_text="Format: '%Y-%m-%d' i.e. 2006-10-25")
    postDate = models.DateTimeField()
    accepted = models.BooleanField(default=False)
    deliveryCost = models.IntegerField(null=True)

    def __str__(self):
        return '%s %s' % (self.author.profileAuthor.username, self.postDate)

    def get_absolute_url_details(self):
        return reverse("order-details", kwargs={'my_id': self.id})

    def get_absolute_url_update(self):
        return reverse('order-update', kwargs={'my_id': self.id})

    def get_absolute_url_delete(self):
        return reverse('order-delete', kwargs={'my_id': self.id})