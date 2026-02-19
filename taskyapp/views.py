from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, "taskyapp/index.html")

