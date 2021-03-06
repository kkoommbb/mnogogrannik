from django.http import HttpResponse

from django.shortcuts import render

from .models import Problem


def index(request):
    latest_problems_list = Problem.objects.order_by('-id')[:5]
    output = '\n'.join([str(item.id) + ' ' + item.name for item in latest_problems_list])
    return HttpResponse(output)

def single_problem(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    output = problem.name + ' ' + problem.task
    return render(request, 'problems/index.html', {'problem': problem})
