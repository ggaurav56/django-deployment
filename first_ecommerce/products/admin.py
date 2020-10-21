from django.contrib import admin
from .models import Product
# Register your models here.

# this is used to autofill the slugfield as you type the title so that you wont have to type always
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)} # new
admin.site.register(Product,ProductAdmin)