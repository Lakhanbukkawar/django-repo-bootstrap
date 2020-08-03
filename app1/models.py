from django.db import models

# Create your models here.
class cust (models.Model):
    cname=models.CharField(max_length=200)
    caddr=models.CharField(max_length=200)
    cmob_no=models.IntegerField()

    def __str__(self):
        return self.cname