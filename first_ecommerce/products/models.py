from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from accounts.models import Account
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=156)
    product_id = models.CharField(max_length=156, unique=True,default="")
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default = 1)
    available = models.BooleanField(default=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to='products/',default="")
    image2 = models.ImageField(upload_to='products/',default="")
    image3 = models.ImageField(upload_to='products/',default="")
    image4 = models.ImageField(upload_to='products/',default="")
    posted_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True,unique=True,)
    favorites = models.ManyToManyField(Account, related_name='favorites',default=None, blank=True)

    def save(self, *args, **kwargs): #used to have readable urls
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self): #considered as good practice
        return self.title

    def get_absolute_url(self): #considered as good practice
        return reverse('products', kwargs={'slug':self.slug})

    class Meta(): #shows the latest product at first
        ordering = ('-posted_at',)