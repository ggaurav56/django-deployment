from django.db import models
from products.models import Product
# Create your models here.
states =(
    ('','Choose...'),
    ('AN','Andaman and Nicobar Islands'),
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CH','Chandigarh'),
    ('CG','Chhattisgarh'),
    ('DD','Dadra and Nagar Haveli and Daman and Diu'),
    ('DL','Delhi'),
    ('GA','Goa'),
    ('GJ','Gujarat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JK','Jammu and Kashmir'),
    ('JH','Jharkhand'),
    ('KA','Karnataka'),
    ('KL','Kerala'),
    ('LA','Ladakh'),
    ('LD','Lakshadweep'),
    ('MP','Madhya Pradesh'),
    ('MH','Maharashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland'),
    ('OD','Odisha'),
    ('PY','Puducherry'),
    ('PB','Punjab'),
    ('RJ','Rajasthan'),
    ('SK','Sikkim'),
    ('TN','Tamil Nadu'),
    ('TS','Telangana'),
    ('TR','Tripura'),
    ('UP','Uttar Pradesh'),
    ('UK','Uttarakhand'),
    ('WB','West Bengal'),

)


class Order(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices=states,default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete = models.CASCADE)
    product = models.ForeignKey(Product, 
                                related_name='order_items',on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity