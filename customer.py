# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    customer_creditscore = models.IntegerField(blank=True, null=True)
    customer_req_loanamount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'
