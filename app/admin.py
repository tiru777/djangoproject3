from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Employee)
admin.site.register(EmployeeDepartment)

class MyToppings(admin.ModelAdmin):
    list_display = ('name','count')

admin.site.register(Toppings,MyToppings)
admin.site.register(Pizza)
admin.site.register(Area)
admin.site.register(Restaurant)
