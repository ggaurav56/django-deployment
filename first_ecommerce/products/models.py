from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=156)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default = 1)
    available = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    posted_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True,unique=True,)

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