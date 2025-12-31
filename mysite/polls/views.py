from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


# def index(request):
#     # print(type(request))
#     # print(request.method)
#     print(request.user)
#     # processing - database, cache, rendering HTML template
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     # get the 5 most recentaly added questions from the database
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]  #DESC 
#     template = loader.get_template("polls/index.html")
#     # output = ", ".join([q.question_text for q in latest_question_list])
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))

# shortcut method for render template
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# Raising a 404 error
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

# a shorcut :  get_object_or_404()
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)