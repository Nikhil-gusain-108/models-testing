from django.db import models

# Create your models here.

# Genra model info-> [genra name]
class Genra(models.Model):
    genra_name=models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.genra_name

# Book model info -> [book name, book genra(relation),book price,avilable,book discription, book image,book reviews(relation many to one)]
class Book(models.Model):
    book_name = models.CharField(max_length=100,null=True, blank=True)
    book_img = models.ImageField(upload_to='media',verbose_name= ("images"), blank=True)
    book_genra= models.ManyToManyField(Genra, verbose_name= ("book_genra"))
    book_price = models.PositiveIntegerField( default=100 ,null=True, blank=True)
    book_avilability = models.BooleanField(default = False,null=True, blank=True)
    book_detail = models.TextField(max_length=500,null=True, blank=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.book_name
    

# user model info ->[ user name, fav book (relation), password, fav genera(relation),profile pic, online timelimit]
