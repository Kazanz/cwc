from django.contrib import admin
from django.core.validators import RegexValidator
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class SignUpData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=255, validators=[phone_regex], blank=True) # validators should be a list

    def __unicode__(self):
        return self.first_name + " " + self.last_name

admin.site.register(SignUpData)
admin.site.register(Course)
