from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

validate_cnic = RegexValidator(r'^[0-9+]{5}-[0-9+]{7}-[0-9]{1}$', 'Not a valid C.N.I.C.')
status = (
    ('karkun', 'karkun'),
    ('umeedwar', 'umeedwar'),
    ('rukn', 'rukn'),
)


class Address(models.Model):
    house = models.CharField(blank=True, max_length=100)
    street = models.CharField(blank=True, max_length=100)
    town = models.CharField(blank=False, max_length=100)
    city = models.CharField(blank=False, max_length=100)
    district = models.CharField(blank=True, max_length=100)


class MemberData(models.Model):
    name = models.CharField(max_length=50, blank=False)
    father_name = models.CharField(max_length=50, blank=False)
    mobile_number = PhoneNumberField()
    email = models.EmailField()
    cnic = models.CharField(validators=[validate_cnic], max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    status_in_jamaat = models.CharField(choices=status,max_length=15)
    designation = models.CharField(max_length=100)
    facebook_url = models.URLField()
    date_of_birth = models.DateField

    def __str__(self):
        return self.name

# Create your models here.
