from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from core.models import User


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
    ('internation_password', "Internation Password")
)


class UserAccount(models.Model):
    id = models.UUIDFIELD(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12,decimal_places=2, default=0.00)
    account_number = models.ShortUUIDField(unique=True,lenght=10,max_lenght=20, prefix='255',alphabet='1234567890')
    account_id = models.ShortUUIDField(unique=True,lenght=10,max_lenght=20, alphabet='1234567890')
    read_code = models.ShortUUIDField(unique=True,lenght=10,max_lenght=20, alphabet='1234567890')
    account_status = models.CharField(choices=ACCOUNT_STATUS , max_length=110, default='in-active')
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirm = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return  self.user



