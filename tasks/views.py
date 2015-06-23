from django.shortcuts import render
from django.http import HttpResponse
from .models import CurrentTask, TaskType
from django.template import Context, loader

def index(request):
    task_list = TaskType.objects.order_by('-date_due')[:20]
    context = {'task_list': task_list}
    return render(request, 'tasks/index.html', context)


