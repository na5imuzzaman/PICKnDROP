from django.urls import path
from ordertrack import views as v


urlpatterns = [
    path('request-form/', v.request_views, name='request-form'),

]