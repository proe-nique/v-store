from django.urls import path
from . import views  

app_name = 'products'

urlpatterns = [
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'), 
    path('all/', views.ProductListView.as_view(), name='product_list'),
    path('create/product/<slug:slug>/', views.ProductCreateView.as_view(), name='create_product'),
    path('delete/product/<slug:slug>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('update/product/<slug:slug>/', views.ProductUpdateView.as_view(), name='update_product'),
]