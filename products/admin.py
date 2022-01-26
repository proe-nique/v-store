from django.contrib import admin
from .models import Product, Category
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name',)
    list_filter = ('name',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('published',)
    prepopulated_fields = {'slug': ['name'],}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)
    list_filter = ('name',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('name',)
    prepopulated_fields = {'slug': ['name'],}