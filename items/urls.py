from django.urls import path
from .views import CreateCheckoutSessionView, ListView, ItemView


urlpatterns = [
    path('', ListView.as_view(), name='All Idem' ),
    path("buy/<int>/", CreateCheckoutSessionView.as_view(), name="Buy"),
    path("item/<int>/", ItemView.as_view(), name="Item"),
]
