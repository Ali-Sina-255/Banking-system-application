from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

from django_extensions.db.fields import ShortUUIDField
from shortuuid.django_fields import ShortUUIDField



class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address.")

        if not username:
            raise ValueError("User must have an Username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return self.is_admin


ACCOUNT_STATUS = (
    ('in-active',"In-Active"),
    ('active','Active'),
)

MARTIUALE_STATUS = (
    ('married',"Married"),
    ('Single', "Single"),
    ('Other', "Other"),
)

GENDER = (
    ('Femail',"Femail"),
    ('Male', "Male"),
    ('Other', "Other"),
)

IDENTITY_TYPE = (
    ('national_id',"National ID"),
    ('internation_passport', "Internation passport")
)


class UserAccount(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user')
    account_balance = models.DecimalField(max_digits=12,decimal_places=2, default=0.00)
    account_number = ShortUUIDField(unique=True, prefix='420', alphabet='1234567890')
    account_id = ShortUUIDField(unique=True, alphabet='1234567890')
    read_code = ShortUUIDField(unique=True, alphabet='asdcxvfgbhre1234567890')
    account_status = models.CharField(choices=ACCOUNT_STATUS , max_length=110, default='in-active')
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirm = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        try:
            return self.user.first_name
        except:
            return "Account model is created"


class KYCModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False,default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=200)
    images = models.ImageField(upload_to='kyc/')
    marrital_status = models.CharField(choices=MARTIUALE_STATUS,max_length=100)
    gender = models.CharField(choices=GENDER, max_length=100)
    identity_id = models.CharField(choices=IDENTITY_TYPE,max_length=100)
    identity_image = models.ImageField(upload_to='kyc/images',null=True, blank=True)
    date_of_birth = models.DateTimeField(auto_now=False)
    signature = models.ImageField(upload_to='key/signature')

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state  = models.CharField(max_length=10)

    mobile =  models.CharField(max_length=255)
    facebook = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.user.first_name} {self.user.last_name}"


