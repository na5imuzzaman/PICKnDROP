from django.urls import path
from homeonly import views as hv
from ordertrack import views as ov

urlpatterns = [
    path('', hv.home_views, name='home'),
    # path('details/<int:my_id>/', hv.order_details_views, name='order-details'),
    path('details/<int:my_id>/update/', ov.update_order_views, name='order-update'),
    # path('details/<int:my_id>/delete/', ov.order_delete_views, name='order-delete'),
]