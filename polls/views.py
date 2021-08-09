# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')
    # response = ', '.join([q.question_text for q in questions])

    # template = loader.get_template("polls/index.html")
    context = {'questions': questions}
    return HttpResponse(render(request, "polls/index.html", context))


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404(f"Question {question_id} does not exist")
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    return HttpResponse(f"You are looking at result of {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
