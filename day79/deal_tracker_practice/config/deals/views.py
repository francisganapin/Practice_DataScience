from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from .models import Deal
from django.urls import reverse_lazy



class DealListView(ListView):
    model = Deal
    template_name = 'deals/deal_list.html'
    context_object_name = 'deals'
    
class DealCreateView(CreateView):
    model = Deal
    fields = ['title','amount','stage']
    template_name = 'deals/deal_form.html'
    success_url = reverse_lazy('deal_list')

class DealUpdateView(UpdateView):
    model = Deal
    fields = ['title','amount','stage']
    template_name = 'deals/deal_form.html'
    success_url = reverse_lazy('deal_list')



