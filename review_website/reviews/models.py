from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# review reply contain --> [text]
class reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    text=models.TextField(max_length=1000)
    id = models.AutoField(primary_key=True)
# reviews model needs = [user who reviewd , user getting reviewed , title , actual review, time of review   ]
class reviews(models.Model):
    reviews_img = models.ImageField(upload_to='media',verbose_name= ("images"), blank=True)
    title = models.CharField( max_length=100)
    text = models.ManyToManyField(reply,blank=True)
    user = models.ManyToManyField(User,blank=True)
    created_time = models.DateTimeField( auto_now=True)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.title} {self.id}"

# user details model conatins --> [user(relation), user type, ]
class user_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    user_type = models.CharField(max_length=50,null=True,blank=True)
    review = models.ManyToManyField(reviews,blank=True)
    created_time = models.DateTimeField( auto_now=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.created_time} {self.id}"
    