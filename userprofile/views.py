from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from .forms import ProfileEditForm
from .models import ProfileEdit
from deliverytrack.models import AcceptOrderRequest


@login_required
def profile_views(request, username):

    try:
        user = User.objects.get(username=username)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        return HttpResponse('<h1>No Such User<h1>')

    try:
        profile = ProfileEdit.objects.get(profileAuthor=user)
        order_status = AcceptOrderRequest.objects.filter(
            orderDetails__author__profileAuthor__username=request.user.username,
        ).order_by('orderDetails__deliveryDate') #delivered=True

        delivery_status = AcceptOrderRequest.objects.filter(
            deliveryMan__profileAuthor__username=request.user.username,
        ).order_by('orderDetails__deliveryDate') #delivered=True

    except (TypeError, ValueError, OverflowError, ProfileEdit.DoesNotExist):
        if request.user.username == username:
            return redirect('edit/')
        else:
            return HttpResponse('<h1>Profile Not Complete</h1>')

    context = {
        'profile': profile,
        'delivery_status': delivery_status,
        'order_status': order_status,
    }

    return render(request, 'profile.html', context)


@login_required
def profile_edit_views(request, username):
    current_user = request.user.username
    try:
        user = User.objects.get(username=username)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        return HttpResponse('<h1>No Such User<h1>')
    # print(current_user, username)

    if current_user == user.username:
        if request.method == 'POST':
            form = ProfileEditForm(request.POST, request.FILES)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.profileAuthor = request.user
                new_form.save()
                return redirect('../')
        form = ProfileEditForm
        return render(request, 'profile_edit.html', {'form': form})
    else:
        return redirect('../')
