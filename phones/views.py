from django.shortcuts import render
from .models import Phones
from django.views.generic import DeleteView, UpdateView, CreateView , ListView, DetailView
from django.urls import reverse_lazy

# Create your views here.
class PhonesListView(ListView):
    template_name='phone/phone_list.html'
    model = Phones
    context_object_name = "Phones"
class PhonesDetailView(DetailView):
    template_name='phone/phone_detail.html'
    model=Phones 
class PhonesCreateView(CreateView):
    template_name = "phone/phone-create.html"
    model = Phones
    fields = ['name','purchaser','desc']  


class PhonesUpdateView(UpdateView):
    template_name = "phone/phone-update.html"
    model = Phones
    fields = ['name','purchaser','desc']     

class PhonesDeleteView(DeleteView):
    template_name = "phone/phone-delete.html"
    model = Phones
    success_url = reverse_lazy("phones_list")
