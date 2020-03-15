from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

def index(request):
    return render(request, 'polls/index.html')

def low_risk(request):
    return render(request, 'polls/low_risk.html')

def phone_call(request):
    return render(request, 'polls/phone_call.html')

def hospital_admission(request):
    return render(request, 'polls/hospital_admission.html')

def advice(request, opt):
    return render(request, 'polls/advice.html', context={"opt":opt})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


def next(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        print(selected_choice.choice_bool)
        if selected_choice.choice_bool:
            if question_id < 4:
                return HttpResponseRedirect(reverse('polls:detail', args=(question_id+1,)))
            else:
                return HttpResponseRedirect(reverse('polls:advice', args=(1,)))
        else:
            if question_id < 4:
                return HttpResponseRedirect(reverse('polls:advice', args=(0,)))
            else:
                return HttpResponseRedirect(reverse('polls:advice', args=(2,)))
