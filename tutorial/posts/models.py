from django.db import models
from django_countries.fields import CountryField


class PostUserDetails(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=264, unique=False)
    country = CountryField()
    isbn = models.CharField(max_length=13)
    bookTitle = models.CharField(max_length=100, null=True)
    bookAuthor = models.CharField(max_length=100, null=True)
    date_Added = models.CharField(max_length=100, null=True)
