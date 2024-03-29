from django.urls import path
from register import views as v
from django.contrib.auth import views as auth_views
from register.forms import LoginForm


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name="login"),
    # path('login/', v.login_views, name='login'),
    path('signup/', v.registration_views, name='signup'),

    path('activate/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/',
         v.activate_account_views,
         name="activate"),

    path('logout/',
         auth_views.LogoutView.as_view(template_name='registration/logout.html'),
         name="logout"),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='reset/password_reset_form.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'), name='password_reset_complete'),

    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='reset/password_change.html'),
         name='password_change'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='reset/password_change_done.html'),
         name='password_change_done'),
]
