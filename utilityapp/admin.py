from django.contrib import admin
from .models import Customer, ServiceRequest

admin.site.register(Customer)
admin.site.register(ServiceRequest)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'type', 'status', 'date_submitted', 'date_resolved')
    list_filter = ('status', 'date_submitted', 'date_resolved')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
