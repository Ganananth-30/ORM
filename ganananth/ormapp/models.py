from django.db import models
from django.contrib import admin
class Amazon(models.Model):
   Product=models.CharField(max_length=25)
   MRP=models.IntegerField()
   Product_Material=models.CharField(max_length=15)
   serial_Number=models.CharField(max_length=10)
   review=models.DateField()
   Phone_Number=models.IntegerField()
   email=models.EmailField()
class AmazonAdmin(admin.ModelAdmin):
    list_display=["Product","MRP","Product_Material","serial_Number","review","Phone_Number","email"]