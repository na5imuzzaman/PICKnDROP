from django.urls import path

from userprofile import views as v


urlpatterns = [

        path('<str:username>/', v.profile_views, name='profile_views'),
        path('<str:username>/edit/', v.profile_edit_views, name='profile_edit_views'),
]
