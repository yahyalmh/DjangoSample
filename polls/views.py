# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')
    # response = ', '.join([q.question_text for q in questions])

    # template = loader.get_template("polls/index.html")
    context = {'questions': questions}
    return HttpResponse(render(request, "polls/index.html", context))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    return HttpResponse(f"You are looking at result of {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
