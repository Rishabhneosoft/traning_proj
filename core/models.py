from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

STATE_CHOICE=((
    ('Python','Python'),
    ('Java','Java'),
    ('React','React'),
    ('Angular','Angular'),
    ('Node','Node'),
    ('PHP','PHP'),

))

STATE_CHOICE1=((
    ('Male','Male'),
    ('Female','Female'),

))

STATE_CHOICE2=((
    ('TL','TL'),
    ('Tranni','Tranni'),

))

STATE_CHOICE3=((
    ('InProcess','InProcess'),
    ('Complete','Complete'),

))

class User(AbstractUser):
    mobile_number = models.CharField(
        max_length=40, unique=True, blank=False, null=False, db_index=True
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    field_type = models.CharField(choices=STATE_CHOICE, max_length=50)
    User_type = models.CharField(choices=STATE_CHOICE2, max_length=50)
    assigned_client = models.CharField(max_length=100)
    DOB = models.DateField(null=True,blank=True)
    gender = models.CharField(choices=STATE_CHOICE1, max_length=50)
    # REQUIRED_FIELDS = ["mobile_number", "email"]

    def __str__(self):
        return f"{self.first_name}/{self.email}"


# class User (models.Model):
#     # fullname = models.CharField(max_length=50)
#     # email = models.EmailField(max_length=50)
#     DOB = models.DateField(null=True,blank=True)
#     gender = models.CharField(choices=STATE_CHOICE1, max_length=50)
#     # password = models.CharField(max_length=50)
#     mobile = models.CharField(max_length=25, null=True, blank=True)
#     address = models.CharField(max_length=250, null=True, blank=True)
#     field_type = models.CharField(choices=STATE_CHOICE, max_length=50)
#     User_type = models.CharField(choices=STATE_CHOICE2, max_length=50)
#     assigned_client = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.fullname}/{self.email}"


class Review(models.Model):
    # date = models.DateField(auto_now=False, auto_now_add=False)
    review = models.TextField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review}'


class Traning(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=STATE_CHOICE3, max_length=50)
    Start_traning_date = models.DateField(auto_now=False, auto_now_add=False)
    End_traning_date = models.DateField(auto_now=False, auto_now_add=False)
    discription = models.TextField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return f'{self.status}/{self.user}'


class Assignment(models.Model):
    # status = models.CharField(choices=STATE_CHOICE2, max_length=50)
    Start_traning_date = models.DateField(auto_now=False, auto_now_add=False)
    End_traning_date = models.DateField(auto_now=False, auto_now_add=False)
    Topic_of_assignment = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Topic_of_assignment}'

class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}/{self.user}'