from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return  HttpResponse("Chào mừng Hoàng Văn Dũng.")

def detail(request, question_id):
    return HttpResponse("You are looking question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're votting on question %s." question_id)
