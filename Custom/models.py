from datetime import datetime
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractBaseUser   , BaseUserManager 
 
class myUserManager(BaseUserManager):
    def create_user(self, name, email, password = None):
        if not name:
            raise ValueError("Please Enter Name")
        if not email:
            raise ValueError("Email is required")
        user  = self.model(
            name = name,
            email = self.normalize_email(email)
        )
        user.set_password(password)

        user.save(using = self._db)
        
        return user
    def create_superuser(self, name, email,password = None):
        user = self.create_user(
            name = name,
             email = self.normalize_email(email),
              password= password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using  = self._db)
        return user
        
class myUser(AbstractBaseUser):

    name = models.CharField(max_length=50, verbose_name=" User Name: ")
    email = models.EmailField(max_length=50,unique=True, verbose_name="E-mail Address :")
    is_active =  models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']
    objects  = myUserManager()
    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj = None):
        
        return self.is_admin
    def has_perms(self, perm, obj= None):
        return True

    def has_module_perms(self, app_label):
        return True


class Author(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class book(models.Model):
    
    title = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author_books")
    

    

    def __str__(self):
        return self.title


class transaction(models.Model):
    user = models.ForeignKey(myUser, related_name="user_transactions", on_delete= models.CASCADE)
    books = models.ForeignKey(book, related_name ="book_transactions",on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    @property
    def price(self):
        book_price = (self.return_date - self.issue_date).days * 10
        return book_price