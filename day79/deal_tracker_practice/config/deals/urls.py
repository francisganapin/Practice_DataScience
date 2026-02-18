from django.url  import path
from .views import DealListView,DealCreateView,DealUpdateView


ulrpatterns = [
    path('',DealListView.as_view(),name='deal_list'),
    path('add.',DealCreateView(),name='deal_add'),
    path('edit/<int:pk>/',DealUpdateView.as_view(), name='deal_edit')
]