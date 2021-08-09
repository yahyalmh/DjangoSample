# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World, you are at polls index")


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You are looking at result of {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
