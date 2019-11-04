from django.shortcuts import render, get_object_or_404, HttpResponse
from userprofile.models import ProfileEdit
from ordertrack.models import PostOrderRequest
from deliverytrack.models import AcceptOrderRequest


def all_mine_views(request):
    try:
        profile = ProfileEdit.objects.get(profileAuthor=request.user)
    except (NameError, ValueError, ProfileEdit.DoesNotExist):
        return HttpResponse('No User Found')

    try:
        allobj = PostOrderRequest.objects.filter(author=profile)
    except (NameError, ValueError, PostOrderRequest.DoesNotExist):
        return HttpResponse('Order Not Found')

    try:
        asdel = AcceptOrderRequest.objects.get(deliveryMan=profile)
    except (NameError, ValueError, AcceptOrderRequest.DoesNotExist):
        return HttpResponse('Error 404 : Not Found')

    try:
        ascus = AcceptOrderRequest.objects.get(orderDetails__author=profile)
    except (NameError, ValueError, AcceptOrderRequest.DoesNotExist):
        return HttpResponse('Error 404 : Not Found')


