# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class FinanceRecord(models.Model):
    stock_no = models.CharField(max_length=6L)
    quarter = models.CharField(max_length=8L)
    stock_name = models.CharField(max_length=10L, blank=True)
    link = models.CharField(max_length=128L, blank=True)
    eps = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    revenue = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
    revenue_growth_byyear = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    revenue_growth_byquar = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    earning = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
    earning_growth_byyear = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    earning_growth_byquar = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    net_assets = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    roe = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    cash_flow_pershare = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    margin = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    issuedate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'finance_record'
