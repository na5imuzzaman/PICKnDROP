from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ordertrack.models import PostOrderRequest
from userprofile.models import ProfileEdit
from deliverytrack.models import AcceptOrderRequest


def home_views(request):

    queryset = PostOrderRequest.objects.filter(
        deliveryDate__range=[datetime.now(), '2080-12-31'], accepted=False).order_by('deliveryDate')

    if request.method == 'POST':
        objid = request.POST.get('id')
        obj = PostOrderRequest.objects.get(id=objid)
        print(obj)

        if request.user.username == obj.author.profileAuthor.username:
            if not obj.accepted:
                obj.delete()
                return redirect('home')
            else:
                return HttpResponse('Already accept by someone or doesn\'t exist.')
        else:
            if request.user.is_anonymous:
                return redirect('login')
            try:
                file = ProfileEdit.objects.get(profileAuthor=request.user)
            except (TypeError, ValueError, ProfileEdit.DoesNotExist):
                return HttpResponse('<h1>Please complete your profile before accept a delivery request.</h1>'
                                    '<h1><a href="../../">Back Home</a></h1>')

            new_form = AcceptOrderRequest()
            new_form.deliveryMan = file
            new_form.orderDetails = obj
            new_form.getDelivery = False
            new_form.pickParcel = False
            new_form.acceptTime = timezone.now()
            new_form.save()
            obj.accepted = True
            obj.save()
            return redirect('deliver-details', new_form.id)

    context = {
        'queryset': queryset

    }
    return render(request, 'homeview.html', context)


# @login_required
# def order_details_views(request, my_id):
#     try:
#         file = ProfileEdit.objects.get(profileAuthor=request.user)
#     except (TypeError, ValueError, ProfileEdit.DoesNotExist):
#         return HttpResponse('<h1>Please complete your profile before accept a delivery request.</h1>'
#                             '<h1><a href="../../">Back Home</a></h1>')
#
#     obj = get_object_or_404(PostOrderRequest, id=my_id)
#     profile = ProfileEdit.objects.get(profileAuthor=obj.author.profileAuthor)
#
#     if request.method == "POST":
#         if file == profile:
#             obj.delete()
#             return redirect('home')
#
#         new_form = AcceptOrderRequest()
#         new_form.deliveryMan = file
#         new_form.orderDetails = obj
#         new_form.getDelivery = False
#         new_form.pickParcel = False
#         new_form.acceptTime = timezone.now()
#         new_form.save()
#         obj.accepted = True
#         obj.save()
#         return redirect('deliver-details', new_form.id)
#
#     context = {
#         'obj': obj,
#         'profile': profile,
#     }
#
#     return render(request, 'order_details.html', context)
#
