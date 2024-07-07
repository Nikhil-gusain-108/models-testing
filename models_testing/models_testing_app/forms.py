from django.forms import ModelForm
from .models import Book


# Creating form from model
class book_form(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
