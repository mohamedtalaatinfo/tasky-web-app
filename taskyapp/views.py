from ast import Delete
from collections.abc import Sequence
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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
    template_name = "taskyapp/complished_details.html"
    model = ComplishedTaskModel
    context_object_name = "task"


class AddTaskView(CreateView):
    model = TaskyModel
    template_name = "taskyapp/add_task.html"
    fields = ['title', 'priority', 'task']
    success_url = '/'



class ComplishedTasksView(View):
    def post(self, request):
        data =  request.POST.getlist('mark-box')
        print(data)
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
    


class EditeTaskView(UpdateView):
    model = TaskyModel
    fields = ['title', 'priority', 'task']
    template_name = 'taskyapp/edite_task.html'
    success_url = '/'


    
    # def get(self, request, pk):
    #     task = TaskyModel.objects.get(pk=pk)
    #     print(task.task)



    #     return render(request, "taskyapp/edite_task.html", {
    #         'task': task
    #     })
    

    # def post(self, request, pk):
    #     title = request.POST.get('title')
    #     priority = request.POST.get('priority')
    #     task = request.POST.get('task')

    #     print(title, priority, task, sep='\n')

    #     TaskyModel.objects.update(title=title, priority=priority, task=task)

    #     return HttpResponseRedirect('/')