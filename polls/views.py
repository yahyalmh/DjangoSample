# Create your views here.
from django.http import HttpResponse

from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')
    response = ', '.join([q.question_text for q in questions])
    return HttpResponse(response)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You are looking at result of {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
