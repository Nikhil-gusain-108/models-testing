from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Genra,Book
from django.shortcuts import get_object_or_404
from random import randint
from .forms import book_form
# Create your views here.
def index(request):
    genras = Genra.objects.all()
    genra_length = len(genras)
    books = Book.objects.all()
    details = {"genra":genras,"books":books,"genere":genras[randint(0,genra_length-1)]}
    return render(request,'index.html',{"details":details})


#function to render books list
def library(request):
    genras = Genra.objects.all()
    books = Book.objects.all()
    details = {"genra":genras,"books":books}
    return render(request,'book_view.html',{"details":details})


#function to show books details
def about(request,book_id):
    books = get_object_or_404(Book,pk = book_id)
    genras = Genra.objects.all()
    details = {"genra":genras,"books":books}
    return render(request,'book_details.html',{"details":details})

# function to sort the books according to genre
def genra_sort(request,genra_id):
    genra= get_object_or_404(Genra,pk = genra_id)
    genras = Genra.objects.all()
    books = Book.objects.all()
    details = {"genras":genra,"books":books,"genra":genras}
    return render(request,'sorted.html',{"details":details})


# update the books details
def edit(request,book_id):
    book = Book.objects.filter(pk = book_id)
    book_data = get_object_or_404(Book,pk = book_id)
    genras = Genra.objects.all()
    if request.method == "POST":
        form = book_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data
            print(name)
            book.update(book_name =name['book_name'])
            book.update( book_price=name['book_price'] )
            book.update( book_price=name['book_price'] )
            book.update( book_detail=name['book_detail'] )
            # book.update(book_name = form.cleaned_data("book_name")
        return HttpResponseRedirect('/library/')
    else:
        form = book_form(instance = book_data)
        details = {"genra":genras,"form":form}
        return render(request,'edit.html',{"details":details})

# Delete the books
def delete(request,book_id):
    book = get_object_or_404(Book,pk = book_id)
    book.delete()
    return HttpResponseRedirect('/library/')

# Add books
def add(request):
    genras = Genra.objects.all()
    if request.method == "POST":
        form = book_form(request.POST)
        if form.is_valid:
            s_form = book_form(request.POST,request.FILES)
            s_form.save()
        return HttpResponseRedirect('/library/')
    else:
        form = book_form()
        details = {"genra":genras,"form":form}
        return render(request,'edit.html',{"details":details})

