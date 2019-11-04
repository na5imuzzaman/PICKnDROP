from django.urls import path
from deliverytrack import views as dv

urlpatterns = [
    path('<int:d_id>/', dv.delivery_details_view, name='deliver-details')
] 
