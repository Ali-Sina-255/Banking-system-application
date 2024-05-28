from django.db import models
from shortuuid.django_fields import ShortUUIDField

from accounts.models import Account
import uuid


# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)


ACCOUNT_STATUS = (
    ('active', "Active"),
    ('in-active', "In-active")
)


MARRITAL_STATUS = (
    ('married',"Married"),
    ('single', "Single"),
    ('Other', "Other"),
)

GENDER = (
    ('male',"Male"),
    ('Female', "Female"),
    ('Other', "Other")

)
IDENTITY_TYPE = (
    ("national_id","National Id Card"),
    ("driver_license", "Driver License "),
    ("national_passport", "National Passport"),
)


class UserAccount(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(lenght=10, max_length=25, prefix='255', alphabet='1234567890')
    account_id = ShortUUIDField(lenght=7, max_length=25, prefix='ali', alphabet='1234567890')
    pin_number = ShortUUIDField(lenght=7, max_length=25, alphabet='123456789')
    red_code = ShortUUIDField(lenght=10, max_length=25, alphabet='123456789')
    account_status = models.CharField(max_length=255, choices=ACCOUNT_STATUS)
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ['-data']
        verbose_name = "UserAccount"
        verbose_name_plural = "UserAccounts"

    def __str__(self):
        try:
            return self.user
        except:
            return "Account Model"


class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/kyc', default='default.jpg')
    marrital_status = models.CharField(choices=MARRITAL_STATUS, max_length=100)
    gender = models.CharField(choices=GENDER, max_length=200)
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=200)
    date_of_birth = models.DateField()
    signature = models.ImageField(upload_to='images/kyc/signature')

    counter = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    mobile = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}"