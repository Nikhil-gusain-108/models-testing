from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import reviews,reply


# form for reviews 
class review_form(ModelForm):
    class Meta:
        model = reviews
        fields=('title','text','reviews_img')
# form for replys
class reply_form(ModelForm):
    class Meta:
        model = reply
        fields= '__all__'
# user registration form
class userRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =('username','password1','password1')