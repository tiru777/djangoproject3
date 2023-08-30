from django.db import models

# Create your models here.

SHIRT_SIZES = [
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
]
class Employee(models.Model):
    """
    Company lo chala mandhi employees untaru
    """

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True,null=True)
    dob_date = models.DateField()
    salary = models.IntegerField()
    address = models.TextField()
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.first_name

class EmployeeDepartment(models.Model):
    """

    Ex: like manufacturer and car
     a Manufacturer makes multiple cars but each Car only has one Manufacturer
    """
    employee_obj = models.ForeignKey(Employee, on_delete=models.CASCADE) # many to one
    department_name = models.CharField(max_length=20)
    department_address = models.TextField()

    def __str__(self):
        return self.department_name

class Toppings(models.Model):
    """
    Toppings ante top of food paina vese vatinii toppings antamu like saas,pepper, chilly
    """
    name = models.CharField(max_length=20)
    count = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    toppings = models.ManyToManyField(Toppings)
    """
    pizza paina kondharu saas vesukuntamu, kondharu chilly vesukuntaru, kondharu saas, chilly anni kallipi vesukuntaru
    """
    pizza_name = models.CharField(max_length=20)

    def __str__(self):
        return self.pizza_name

class Area(models.Model):
    area_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.area_name

class Restaurant(models.Model):
    area = models.OneToOneField(Area,on_delete=models.PROTECT)
    owner_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.owner_name




