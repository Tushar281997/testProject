from django.db import models

# Create your models here.
class VendorMaster(models.Model):
    reclaim_vendor_id = models.CharField(max_length=50)
    ap_vendor_id = models.CharField(max_length=50)
    ap_vendor_number = models.CharField(max_length=50)
    ap_vendor_name = models.CharField(max_length=255)
    ap_vendor_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    inactive_date = models.DateField(null=True, blank=True)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.EmailField()
    customer_vendor = models.CharField(max_length=255)
    swell_flag = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    client = models.CharField(max_length=100)
    reclaim_inactive_date = models.DateField(null=True, blank=True)
    auth_for_debt = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    apply_max_vend_cost = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    auth_reason = models.CharField(max_length=255)
    comments = models.TextField(null=True, blank=True)
    last_scan = models.DateField(null=True, blank=True)
    scans_per_week = models.PositiveIntegerField(default=0)
    dollars_per_week = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    on_hold = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    vendor_type_def = models.CharField(max_length=100)

    def __str__(self):
        return self.ap_vendor_name