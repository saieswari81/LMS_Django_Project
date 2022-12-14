# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LoanRules(models.Model):
    loan_rule_id = models.IntegerField(primary_key=True)
    loan = models.ForeignKey('LoanMaster', models.DO_NOTHING, blank=True, null=True)
    creditscore_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    creditscore_offset = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_offset = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    interest = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    duration_months = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_rules'
