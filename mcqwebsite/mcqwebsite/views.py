from django.shortcuts import render

# Write views function 

def home(request):
    return render(request,'index.html')