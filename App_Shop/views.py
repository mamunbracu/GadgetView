from django.shortcuts import render
from App_Shop.models import Product
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class product_detailes(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/products.html'

