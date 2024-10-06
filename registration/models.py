from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_softdelete.models import SoftDeleteModel

from registration.enums import GenderEnum, MaritalStatusEnum, ResidentStatusEnum


class SharedFieldsModel(SoftDeleteModel):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='created_%(class)s')
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='modified_%(class)s')
    source = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


# User model
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, SharedFieldsModel):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Church(SharedFieldsModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Emirate(SharedFieldsModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MainArea(SharedFieldsModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubArea(SharedFieldsModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Family Model
class Family(SharedFieldsModel):
    church = models.ForeignKey(Church, on_delete=models.SET_NULL, null=True)
    emirate = models.ForeignKey(Emirate, on_delete=models.SET_NULL, null=True)
    main_area = models.ForeignKey(MainArea, on_delete=models.SET_NULL, null=True)
    sub_area = models.ForeignKey(SubArea, on_delete=models.SET_NULL, null=True)
    address_line = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


class FatherConf(SharedFieldsModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProfessionCategory(SharedFieldsModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Member Model
class Member(SharedFieldsModel):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True, related_name='family')
    parent_family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True, blank=True, related_name='parent_family')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    english_name = models.CharField(max_length=100)
    arabic_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GenderEnum.choices())
    marital_status = models.CharField(max_length=15, choices=MaritalStatusEnum.choices())
    father_conf = models.ForeignKey(FatherConf, on_delete=models.SET_NULL, null=True, blank=True)
    profession_category = models.ForeignKey(ProfessionCategory, on_delete=models.SET_NULL, null=True, blank=True)
    profession_name = models.CharField(max_length=100, null=True, blank=True)
    resident_status = models.CharField(max_length=20, choices=ResidentStatusEnum.choices(), null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    seek_for_job = models.BooleanField(default=False)
