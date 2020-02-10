from django.db import models


class Client(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'clients'
