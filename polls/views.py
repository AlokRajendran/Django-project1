from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView




def index(request):
    return HttpResponse("Hello")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"q": question}
    return render(request,"polls/detail.html", context)


def results(request, question_id):
    response = f"Result for question id {question_id} "
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"q":question})
    # return HttpResponse(response)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = request.POST["choice"]
        print(choice, "choice")
        selected_choice = get_object_or_404(Choice, pk=choice)
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "q":question, "error_message": "option not selected"
        })
    selected_choice.votes +=1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
    # return HttpResponse(f" voting on question id {question_id} ")


def questions(request):
    questions = Question.objects.all()
    #output = []
    #for q in questions:
    #    output.append(q.question_text)
    #output = ",".join(output)
    context = {"questions": questions , "content":"<h1>Polls App</h1>"}
    return render(request, "polls/index.html", context)


class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.all()
        

class Detail(DetailView):
    template_name = "polls/detail.html"
    context_object_name = "q"
    model = Question


class Results(DetailView):
    template_name = "polls/results.html"
    context_object_name = "q"
    model = Question



    












