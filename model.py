from django.db import models
# Create your models here.
class Customer(models.Model):
    # It represents a customer in the e-commerce system with fields: 
    # name: the name of the customer
    # email: the email of the customer(should be unique to each customer) 
    # phone number: the phone number of the customer
    # address: the address of the customer
    # created_at: the date and time when the customer was created

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    # It represents an order in the e-commerce system with fields:
    # customer: ForeignKey to the Customer model (one-to-many relationship).
    # order_date: Date when the order was placed.
    # total_amount: Total monetary value of the order.
    # shipping_address: Address where the order will be shipped.
    # created_at: Date and time when the order was created.

    customer = models.ForeignKey(Customer, 
                                 on_delete=models.CASCADE,
                                 related_name='orders'
                                 )
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    