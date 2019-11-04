from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from userprofile.models import ProfileEdit
from ordertrack.models import PostOrderRequest


class AcceptOrderRequest(models.Model):
    deliveryMan = models.ForeignKey(ProfileEdit, on_delete=models.CASCADE)
    orderDetails = models.OneToOneField(PostOrderRequest, on_delete=models.CASCADE, null=True)
    acceptTime = models.DateTimeField(auto_now=True)
    delivered = models.BooleanField(default=False)
    deliveryTime = models.DateTimeField(null=True, blank=True)
    pickParcel = models.BooleanField()
    getDelivery = models.BooleanField()

    def __str__(self):
        return '%s %s' % (self.orderDetails.author.profileAuthor.username, self.deliveryMan.profileAuthor.username)

    def get_absolute_url_details(self):
        return reverse('deliver-details', kwargs={'d_id': self.id})