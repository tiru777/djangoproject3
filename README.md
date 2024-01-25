```commandline
django-admin startproject djangoproject3
django-admin startapp app
```

```commandline
write models in models.py file and register models in admin
```

```commandline
python manage.py createsuperuserE
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


```commandline

login to /admin with your credentials
```

```ForeignKey

Many-to-one relationships is ForeignKey

ForeignKey requires a positional argument: the class to which the model is related.

For example, if a Car model has a Manufacturer – that is, 
 a Manufacturer makes multiple cars but each Car only has one Manufacturer – use the following definitions:

class Manufacturer(models.Model):
    # ...
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

field = models.ForeignKey(Employee, on_delete=models.CASCADE)

This is the behaviour to adopt when the referenced object is deleted.
It is not specific to Django; this is an SQL standard. 
Although Django has its own implementation on top of SQL.

There are seven possible actions to take when such event occurs:

CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)
SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.
SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION


```

```Many To Many Relationship


if a Pizza has multiple Topping objects – that is, 
a Topping can be on multiple pizzas and each Pizza has multiple toppings 
    - Toppings ante top of food paina vese vatinii toppings antamu like saas,pepper, chilly
    - Pizza paina kondharu saas vesukuntamu, kondharu chilly vesukuntaru, kondharu saas, chilly anni kallipi vesukuntaru

    class Topping(models.Model):
        # ...
        pass
    
    
    class Pizza(models.Model):
        # ...
        toppings = models.ManyToManyField(Topping)
        
```

```OneToOneField Relationshionship

For example, if you were building a database of “places”, 
    you would build pretty standard stuff such as address, phone number, etc. in the database. 
    Then, if you wanted to build a database of restaurants on top of the places, 
    instead of repeating yourself and replicating those fields in the Restaurant model,
    you could make Restaurant have a OneToOneField to Place (because a restaurant “is a” place; in fact, 
    to handle this you’d typically use inheritance, which involves an implicit one-to-one relation).

```