from django.db import models

# Create your models here.

#collect or category

class collect(models.Model):
    title = models.CharField(max_length=255)
    feature_prodect = models.ForeignKey('product', on_delete=models.SET_NULL, null=True, related_name='+')

#promotion 
class promation(models.Model):
    discription = models.CharField(max_length=255)     
    discount = models.DecimalField(max_digits=6, decimal_places=2)

#product table
class product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(default='-')
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventry = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collect = models.ForeignKey(collect, on_delete= models.PROTECT)
    promations = models.ManyToManyField(promation)

#customer
class customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILSER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILSER, 'Silver'),
        (MEMBERSHIP_GOLD , 'Gold')

    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=10, choices= MEMBERSHIP_CHOICE , default= MEMBERSHIP_BRONZE)
    


#ORDER
class order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICE = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    place_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices= PAYMENT_STATUS_CHOICE , default= PAYMENT_STATUS_PENDING)

    customer = models.ForeignKey(customer, on_delete= models.PROTECT)

#orderItem
class orderitem(models.Model):
    order = models.ForeignKey(order, on_delete= models.PROTECT)
    product = models.ForeignKey(product, on_delete=models.PROTECT)
    quentity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

#ADDRESS
class address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    zip = models.CharField(max_length=50)

#cart
class cart(models.Model):
    create_at = models.DateField(auto_now_add=True)

#cartItem
class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()    

