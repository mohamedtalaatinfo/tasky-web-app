from collections.abc import Sequence
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .models import TaskyModel

# Create your views here.


class IndexView(ListView):
    model = TaskyModel
    template_name = "taskyapp/index.html"
    context_object_name = "data"

    ordering = ['-pk']



class TaskDetailsView(DetailView):
    template_name = "taskyapp/task_details.html"
    model = TaskyModel
    context_object_name = "task"



class AddTaskView(CreateView):
    model = TaskyModel
    template_name = "taskyapp/add_task.html"
    fields = ['title', 'priority', 'task', 'complished']
    success_url = '/'