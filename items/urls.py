from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.get_session_id, name='get_session_id'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
]