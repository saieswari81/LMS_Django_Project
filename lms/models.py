from django.db import models

# Create your models here.


class LoanMaster(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=200)
    loan_desc = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'loan_master'

    def __str__(self):
        return str(self.loan_id) + self.loan_type


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    application_date = models.DateField(blank=True, null=True)
    customer_creditscore = models.IntegerField(blank=True, null=True)
    customer_req_loanamount = models.DecimalField(max_digits=65535, decimal_places=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.customer_name


class LoanRules(models.Model):
    loan_rule_id = models.IntegerField(primary_key=True)
    loan = models.ForeignKey(LoanMaster, on_delete=models.DO_NOTHING, blank=True, null=True)
    creditscore_limit = models.DecimalField(max_digits=65535, decimal_places=20, blank=True, null=True)
    creditscore_offset = models.DecimalField(max_digits=65535, decimal_places=20, blank=True, null=True)
    amount_limit = models.DecimalField(max_digits=65535, decimal_places=20, blank=True, null=True)
    amount_offset = models.DecimalField(max_digits=65535, decimal_places=20, blank=True, null=True)
    interest = models.DecimalField(max_digits=65535, decimal_places=20, blank=True, null=True)
    duration_months = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_rules'


class CustomerLoansStatus(models.Model):
    customer_loan_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    loan = models.ForeignKey(LoanMaster, on_delete=models.DO_NOTHING, blank=True, null=True)
    loan_status = models.CharField(max_length=200, blank=True, null=True)
    approved_interest = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    approved_duration_months = models.IntegerField(blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_loans_status'

    def __str__(self):
        return self.customer.customer_name + '-' + self.loan.loan.loan_type + '-' + self.loan_status
