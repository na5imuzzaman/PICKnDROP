from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from .token_generator import activation_token


def registration_views(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False

            user_email = form.cleaned_data.get("email")
            user.save()

            get_site = get_current_site(request)
            email_subject = "Activate The Account."
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': get_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': activation_token.make_token(user),
            })

            email = EmailMessage(email_subject, message, to=[user_email])
            email.send()
            return render(request, 'registration/signup_done.html', {})

    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def activate_account_views(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and activation_token.check_token(user, token):
        # May need to change here. may need an xtra field to mark verified mail.
        user.is_active = True
        user.save()
        return HttpResponse('<h2>Your email successfully verified. '
                            'We will cross-check your identity & notify you in shortly. '
                            'Thank you for your patience</h2>'
                            )
    else:
        return HttpResponse('<h1>Activation link is invalid.</h1>')
