from django.db import models
from django.utils.timezone import localtime
from django.contrib.auth.models import User

# Write django models here

# quiz types need --> [ type name,id ]
class Quiz_types(models.Model):
    type_name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.type_name}"
#quiz name have --[quiz name, id]
class Q_name(models.Model):
    quiz_name = models.CharField( max_length=50)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.quiz_name} {self.id}"
# Optons model need --> [id ,quiz_name,quiz question, option A,option B, option C, option D]
class options(models.Model):
    quiz_name = models.ManyToManyField(Q_name)
    quiz_question = models.CharField( max_length=100,blank=True)
    option_A = models.CharField( max_length=50)
    option_B = models.CharField( max_length=50)
    option_C = models.CharField( max_length=50)
    option_D = models.CharField( max_length=50)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.quiz_question} {self.id}"
# Quiz model need --> [id, question, answer, options, quiz_name]
class quiz(models.Model):
    quiz_name = models.ManyToManyField(Q_name)
    question = models.CharField( max_length=100)
    answer = models.CharField( max_length=100)
    options = models.OneToOneField(options, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.question} {self.id}"
# Quiz data model need --> [id, quiz name(relation), quiz type(relation), quiz(relation), creator(relation), details]
class quiz_data(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_name = models.ManyToManyField(Q_name)
    quiz_type = models.OneToOneField(Quiz_types,on_delete=models.CASCADE)
    quiz = models.ManyToManyField(quiz)
    quiz_creator = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz_details = models.TextField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.quiz_creator.username} {self.id}"
# Quiz history model need --> [id, quiz name(relation), score, user(relation), quiz(relation)]
class quiz_history(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_name = models.ManyToManyField(Q_name)
    quiz = models.ForeignKey(quiz_data , on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz_score = models.IntegerField(default= 0)
    def __str__(self):
        return f"{self.user.username}score{self.quiz_score} {self.id}" 


