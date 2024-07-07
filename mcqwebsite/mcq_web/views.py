from django.shortcuts import render,get_object_or_404, redirect
from .models import quiz_data,quiz_history,Quiz_types
from .forms import userRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# function to show quiz by type
@login_required
def quizes(request,quiz_type_id):
    quiz_type = get_object_or_404( Quiz_types,pk = quiz_type_id)
    quizes = quiz_data.objects.all()
    quiz_types = Quiz_types.objects.all()
    name = None
    for quiz in quizes:
        for quz in quiz.quiz_name.all():
            name = quz.quiz_name
    details = {'quiz':quizes,'quiz_type':quiz_type,'quiz_types':quiz_types,"name":name}
    return render(request,'shorted_show_quiz.html',{'details':details})
# function to add new users
def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid:
            User = form.save(commit = False)
            User.set_password(form.cleaned_data['password1'])
            User.save()
            login(request,User)
    else:
        form = userRegistrationForm()
    return render(request,'registration/register.html',{"form":form})
# function to show quiz by type
@login_required
def show_quiz(request):
    quizes = quiz_data.objects.all()
    quiz_types = Quiz_types.objects.all() 
    user = User.objects.all()
    name = None
    for quiz in quizes:
        for quz in quiz.quiz_name.all():
            name = quz.quiz_name
    details = {'quiz':quizes,'quiz_types':quiz_types,'user':user,"name":name}
    return render(request,'show_quiz.html',{'details':details})
# Function to take quiz
@login_required
def quize(request,quiz_id):
    #if form is being submitted
    if request.method == "POST":
        quizes = quiz_data.objects.all()
        history = quiz_history()
        history.user = request.user
        # not validaing form to handel if user does not fill all forms
        for quz in quizes:
            for item in request.POST:
                for quiz in quz.quiz.all():
                    if quiz.question == item:
                        if quiz.answer == request.POST[item]:
                            history.quiz_score += 1
                        history.quiz = quz
        history.save()
        # cannot create relation befor creatinf the model
        for quz in quizes:
            for item in request.POST:
                for quiz in quz.quiz.all():
                    if quiz.question == item:
                        name =quz.quiz_name
                        for nm in name.all():
                            history.quiz_name.add(nm.id)# to create relations id is needed
        return redirect('/mcq_web/')
    else:
        quizData = get_object_or_404(quiz_data,pk = quiz_id)
        return render(request,'quiz.html',{'quiz_data':quizData.quiz.all()})
# function for leaderbord
def leaderbord(request):
    Q_history = quiz_history.objects.all()
    history_list = Q_history.order_by('-quiz_score')
    name = None
    for player in history_list.all():
        for quiz in player.quiz_name.all():
            name = quiz.quiz_name
    return render(request,'leaderboard.html',{"history":history_list,"quiz_name":name})


