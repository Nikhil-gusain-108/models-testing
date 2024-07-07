from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# user registration form
class userRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =('username','password1','password1')


# # Creating form from model
# class user_form(ModelForm):
#     class Meta:
#         model = user
#         fields = '__all__'