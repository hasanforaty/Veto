from django.http import HttpResponse
from django.shortcuts import (
    render,
    get_object_or_404
)

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(render(request, "polls/index.html", context))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    response = f"you are looking at the result of question ${question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"you are voting on question ${question_id}")
