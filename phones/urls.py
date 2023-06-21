from django.urls import path
from .views import PhonesListView, PhonesDetailView, PhonesCreateView, PhonesUpdateView, PhonesDeleteView

urlpatterns = [
    path('phone/', PhonesListView.as_view(), name='phones_list'),
    path('phone/<int:pk>/', PhonesDetailView.as_view(), name='phones_detail'),
    path('phone/create/', PhonesCreateView.as_view(), name='phones_create'),
    path('phone/<int:pk>/update/', PhonesUpdateView.as_view(), name='phones_update'),
    path('phone/<int:pk>/delete/', PhonesDeleteView.as_view(), name='phones_delete'),
]