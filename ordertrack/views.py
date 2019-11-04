from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from userprofile.models import ProfileEdit
from .forms import PostOrderRequestForm
from ordertrack.models import PostOrderRequest
from ordertrack.delivery_charge import DeliveryCharge


@login_required
def request_views(request):

    try:
        obj = ProfileEdit.objects.get(profileAuthor=request.user)
    except (TypeError, ValueError, ProfileEdit.DoesNotExist):
        return HttpResponse('<h1>Please complete your profile before make a delivery request.</h1>'
                            '<h1><a href="../../">Back Home</a></h1>')

    if request.method == 'POST':
        form = PostOrderRequestForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = obj
            dis = form.cleaned_data.get('pickupPoint')
            unit = form.cleaned_data.get('weight')
            cost = DeliveryCharge()
            charge = cost.cost_counting(dis, float(unit))
            print(charge)
            new_form.deliveryCost = int(charge)
            new_form.postDate = timezone.now()
            new_form.save()

            new_form.save()
            objt = PostOrderRequest.objects.filter(author=obj).last()

            return render(request, 'redirected/order_redirect.html', {})
    form = PostOrderRequestForm()
    context = {
        'form': form,
    }
    return render(request, 'requestform/request_form.html', context)


@login_required
def update_order_views(request, my_id):
    obj = get_object_or_404(PostOrderRequest, id=my_id)

    if obj.accepted:
        return HttpResponse('<h1>Not Authorized</h1>')
    initial_data = {
        'pickupPointType': obj.pickupPointType,
        'pickupPoint': obj.pickupPoint,
        'deliveryPoint': obj.deliveryPoint,
        'parcelType': obj.parcelType,
        'parcelDescription': obj.parcelDescription,
        'weight': obj.weight,
        'deliveryDate': obj.deliveryDate,
    }

    form = PostOrderRequestForm(request.POST or None, initial=initial_data, instance=obj)

    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.postDate = timezone.now()
        dis = form.cleaned_data.get('pickupPoint')
        unit = form.cleaned_data.get('weight')
        cost = DeliveryCharge()
        charge = cost.cost_counting(dis, float(unit))
        print(charge)
        new_form.deliveryCost = int(charge)
        new_form.save()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'requestform/request_form.html', context)


@login_required
def order_delete_views(request, my_id):
    obj = get_object_or_404(PostOrderRequest, id=my_id)

    if obj.accepted:
        return HttpResponse('<h1>Not Authorized</h1>')

    if request.POST:
        obj.delete()
        return redirect('home')

    return render(request, 'order_delete.html', {})