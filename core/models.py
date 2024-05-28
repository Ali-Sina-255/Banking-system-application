from django.db import models
from shortuuid.django_fields import ShortUUIDField

from accounts.models import Account


# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)


ACCOUNT_STATUS = (
    ('active',"Active"),
    ('in-active', "In-active")
)


class UserAccount(models.Model):
    # id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4, editable=False)
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