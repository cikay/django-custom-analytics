from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
class UserManager(BaseUserManager):

    def create_user(self, email, firstname, lastname, password=None):

        if firstname is None:
            raise TypeError('Kullanıcı ismi gerekli')
       
        if lastname is None:
            raise TypeError('Kullanıcı soy ismi gerekli')
        if email is None:
            raise TypeError('Email gerekli')
        
        
        user = self.model(
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, firstname, lastname, password=None):
        user = self.create_user(
            email=email,
            firstname=firstname,
            lastname=lastname,
            password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('firstname', 'lastname')

    objects = UserManager()

    def get_short_name(self):
        return "short name"

    def __str__(self):
        return self.email
    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True
