from django.db.models import *

# Create your models here.
class Hour(Model):
    open=IntegerField(default=0)
    close=IntegerField(default=0)
    
    def __str__(self):
        return str(self.open) + "-" + str(self.close)

class City(Model):
    name=CharField(max_length=256,blank=False)
    image=ImageField(upload_to='static/img')
    description=CharField(max_length=10000,default="No description")
    class Meta:
        verbose_name_plural = 'cities'
    def __str__(self):
        return self.name


class Address(Model):
    street_address=CharField(max_length=256,blank=False)
    city=ForeignKey(City,on_delete=CASCADE)
    class Meta:
        verbose_name_plural = 'addresses'
    def __str__(self):
        return self.street_address + ", " +self.city.name
    
class Place(Model):
    name=CharField(max_length=256,blank=False)
    description=CharField(max_length=1000)
    hour=ForeignKey(Hour, on_delete=CASCADE)
    addr=ForeignKey(Address, on_delete=CASCADE,blank=False)
    class Meta:
        abstract = True
    def __str__(self):
        return type(self).__name__ + self.name
class Hotel(Place):
    rooms_left=IntegerField(default=0)
