from django.urls import path
from .views import CarrierList, CarrierDetail

urlpatterns = [
    path("", CarrierList.as_view(), name="carrier_list"),
    path("<int:pk>/", CarrierDetail.as_view(), name="carrier_detail"),
]
