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
   