# utilityapp/models.py

from django.db import models
from .models import Customer

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    # Add more fields as needed

    class Meta:
        app_label = 'utilityapp'  # Specify the app_label for the model

    def __str__(self):
        return self.name

# utilityapp/models.py


class ServiceRequest(models.Model):
    TYPE_CHOICES = [
        ('Gas Connection', 'Gas Connection'),
        ('Gas Leak', 'Gas Leak'),
        ('Billing Issue', 'Billing Issue'),
        # Add more choices as needed
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    details = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
    # Add more fields as needed

    def __str__(self):
        return f"{self.customer.name}'s {self.type} Request"
