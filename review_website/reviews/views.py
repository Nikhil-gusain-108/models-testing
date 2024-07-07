from django.shortcuts import render, redirect,get_object_or_404
from.models import reviews , user_details,reply
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import review_form,userRegistrationForm,reply_form
# Create your views here.

#function to show own review
@login_required
def show_reviews(request):
    current_user = request.user
    user_detail = user_details.objects.all()
    review = None
    for Users in user_detail:
        if current_user == Users.user:
            review = Users.review.all()
    return render(request,'own_review.html',{"review":review})

#function to show  products for reviews
@login_required
def product_review_section(request):
    review = reviews.objects.all()
    return render(request,'all_review.html',{'review':review})


# function to add product for review
@login_required
def add_product(request):
    if request.method == 'POST':
        UserDetail = user_details.objects.all()
        CurrentUser = request.user
        form = review_form(request.POST,request.FILES)
        if form.is_valid:
            obj = form.save()
            obj.user.add(CurrentUser.id)
            for users in UserDetail.all():
                if users.user == CurrentUser:
                    users.review.add(obj)
        return redirect('all_reviews')
    else:
        form = review_form()
        return render(request,'add_review.html',{'form':form})

# function for new user registration
def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid:
            User = form.save(commit = False)
            User.set_password(form.cleaned_data['password1'])
            User.save()
            user_details.objects.create(user = User)
            login(request,User)
            return redirect('all_reviews')
    else:
        form = userRegistrationForm()
    return render(request,'registration/register.html',{"form":form})

# function to delete reviews
@login_required
def delete(request,review_id):
    review = get_object_or_404(reviews,pk = review_id)
    review.delete()
    return redirect('all_reviews')


# function to make review
@login_required
def comment(request,review_id):
    review = get_object_or_404(reviews,pk = review_id)
    if request.method == "POST":
        form = reply_form(request.POST)
        if form.is_valid:
            obj = request.POST["text"]
            obj = reply.objects.create(user = request.user , text = obj)
            review.text.add(obj.id)
        return redirect('all_reviews')
    else:
        form = reply_form()
        return render(request,"new_comment.html",{"review":review,"form":form})


# function to read comments
@login_required
def readcomment(request,review_id):
    review = get_object_or_404(reviews,pk = review_id)
    user_detail= user_details.objects.all()
    details= None
    for users in user_detail:
        if users.user== request.user:
            details = users
    replys = review.text.all() 
    return render(request,"read_comments.html",{"replys":replys,"review":review})

#function to update comment 
def cmt_update(request,cmt_id):
    replys = get_object_or_404(reply,pk = cmt_id)
    if request.method == "POST":
        print(replys.text)
        replys.text = request.POST["text"]
        print(replys.text)
        replys.save()

    return redirect('all_reviews')

#delete comment 
def cmt_delete(request,cmt_id):
    review = get_object_or_404(reply,pk = cmt_id)
    review.delete()
    return redirect('all_reviews')