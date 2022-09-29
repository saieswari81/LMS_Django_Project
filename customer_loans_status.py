# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CustomerLoansStatus(models.Model):
    customer_loan_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    loan = models.ForeignKey('LoanMaster', models.DO_NOTHING, blank=True, null=True)
    loan_status = models.CharField(max_length=200, blank=True, null=True)
    approved_interest = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    approved_duration_months = models.IntegerField(blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_loans_status'
