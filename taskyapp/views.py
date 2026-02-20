from ast import Delete
from collections.abc import Sequence
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .models import ComplishedTaskModel, TaskyModel

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



class ComplishedDetailsView(DetailView):
    template_name = "taskyapp/task_details.html"
    model = ComplishedTaskModel
    context_object_name = "task"


class AddTaskView(CreateView):
    model = TaskyModel
    template_name = "taskyapp/add_task.html"
    fields = ['title', 'priority', 'task', 'complished']
    success_url = '/'



class ComplishedTasksView(View):
    def post(self, request):
        data =  request.POST.getlist('mark-box')
        for idd in data:
            record = TaskyModel.objects.get(pk=idd)
            title = record.title
            date = record.date
            priority = record.priority
            task = record.task

            ComplishedTaskModel.objects.create(title=title, date=date, priority=priority, task=task)
            record.delete()



        return HttpResponseRedirect('/')
    



class ComplishedListView(View):
    def get(self, request):
        data = ComplishedTaskModel.objects.all()


        return render(request, "taskyapp/complished_list.html", {
            "data": data
        })
    
