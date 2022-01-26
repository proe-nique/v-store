from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib import messages
from .filters import ProductFilter
# Create your views here.


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "create-product.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.name} has been successfully created.")
        return super(ProductCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'create-product'
        return context
    

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "update-product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'update-product'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.name} has been successfully updated.")
        return super(ProductUpdateView, self).form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "confirm-delete-product.html"
    success_url = reverse_lazy('base:home')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'confirm delete product'
        return context

    def form_valid(self, form):
        #form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.name} has been successfully Deleted.")
        return super(ProductDeleteView, self).form_valid(form)

class ProductListView(ListView):
    model = Product
    paginate_by = 20
    context_object_name = 'products'
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context["page_title"] = 'products'
        return context
    
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'product'
        return context
    
    
    