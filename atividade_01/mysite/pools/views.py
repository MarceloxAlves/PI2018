from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return  render(request,'index.html',{"questions": Question.objects.order_by('-pub_date')})

def manager(request,question_id):
    return render(request, 'manage.html', {"question": Question.objects.get(id=question_id), "unrelated" : Choice.unrealted()})

def exibir_question(request, question_id):
    question  =  Question.objects.get(id=question_id)
    if question.closed:
        return redirect('home')
    return  render(request,'question.html',{"question": question})

def question_closed(request, question_id):
    question = Question.objects.get(id=question_id)
    question.is_close()
    return redirect('manage', question_id = question_id)

def vote(request, question_id, choice_id):
    choice  = Choice.objects.get(id=choice_id)
    choice.vote()
    return  render(request,'question.html',{"question": Question.objects.get(id=question_id), "voted":True})

def choice_attach(request, question_id, choice_id):
    choice  = Choice.objects.get(id=choice_id)
    question = Question.objects.get(id=question_id)
    choice.attach(question)
    return redirect('manage', question_id = question_id)

def choice_remove(request, question_id, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.remove()
    return redirect('manage', question_id=question_id)

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {"question": question})

def question_add(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form  = QuestionForm()

    return render(request, 'question-add.html',{"form": form})

def choice_add(request):
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form  = ChoiceForm()

    return render(request, 'choice-add.html',{"form": form})
