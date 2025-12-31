from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# def index(request):
#     # print(type(request))
#     # print(request.method)
#     print(request.user)
#     # processing - database, cache, rendering HTML template
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    # get the 5 most recentaly added questions from the database
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  #DESC 
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)