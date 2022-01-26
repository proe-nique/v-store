from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from django.utils.translation import gettext_lazy as _






class Category(models.Model):
    
    name = models.CharField(default='', max_length=50)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"slug": self.slug})


class Product(models.Model):

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    #tags = models.ManyToManyField("index.Tag", related_name='products')
    name = models.CharField(default='', max_length=50)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(default='products/default.png', upload_to='products')
    price = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    sale_price = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    price_range_from = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    price_range_to = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    published = models.DateTimeField(auto_now=True, auto_now_add=False)
    views = models.PositiveIntegerField(default=0)
    unique = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    fancy = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.user.username + self.name)
        return super().save(*args, **kwargs)