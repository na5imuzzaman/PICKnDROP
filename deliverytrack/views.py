from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from deliverytrack.models import AcceptOrderRequest


@login_required
def delivery_details_view(request, d_id):
    obj = get_object_or_404(AcceptOrderRequest, id=d_id)

    if request.method == 'POST':
        if request.user == obj.deliveryMan.profileAuthor:
            obj.pickParcel = True
            obj.save()
        elif obj.pickParcel and request.user == obj.orderDetails.author.profileAuthor:
            obj.getDelivery = True
            obj.delivered = True
            obj.save()

    context = {
        'obj': obj
    }
    return render(request, 'delivery_details.html', context)