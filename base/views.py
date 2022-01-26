#from django.shortcuts import render

from django.views.generic import TemplateView
from products.models import Product

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(unique=True).all()
        context["page_title"] = 'home'
        return context
    


class About(TemplateView):
    template_name = "about.html"


class Contact(TemplateView):
    template_name = "contact.html"


class Faq(TemplateView):
    template_name = "faq.html"


class Pricing(TemplateView):
    template_name = "pricing.html"

