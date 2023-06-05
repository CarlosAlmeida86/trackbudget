from django.db import models


class Expense(models.Model):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    value = models.FloatField()
    date = models.DateField()
    status = models.BooleanField(verbose_name='Paid?')

    def __str__(self):
        return f'{self.type} = ${self.value}'
