from django.shortcuts import render, redirect
# write views here


# function to render home / layout page
def home(request):
    return render(request,"layout.html")