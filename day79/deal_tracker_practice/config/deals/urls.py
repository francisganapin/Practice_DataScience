from django.urls import path,reverse_lazy
from .views import DealListView,DealCreateView,DealUpdateView


urlpatterns = [
    path('',DealListView.as_view(),name='deal_list'),
    path('add',DealCreateView.as_view(),name='deal_adds'),
    path('edit/<int:pk>/',DealUpdateView.as_view(), name='deal_edit')
]