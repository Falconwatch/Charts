from django.db import models

# Create your models here.
class report_counts(models.Model):
    load_date = models.DateField()
    report_date = models.DateField()
    product_type = models.CharField(max_length=200)
    in_default = models.IntegerField()
    healthy = models.IntegerField()
    will_default = models.IntegerField()
    deleted = models.BooleanField(default=False)