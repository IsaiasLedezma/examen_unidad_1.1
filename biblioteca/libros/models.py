from __future__ import unicode_literals

from django.db import models

# Create your models here.

class libro(models.Model):
    name = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    editorial = models.CharField(max_length=120)
    ISBN = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits = 9999, decimal_place = 2)

    def __unicode__(self):
        return self.name
