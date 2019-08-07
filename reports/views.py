from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from django.http import HttpResponse
### import models to supply the data

class IndexView(generic.ListView):
    def get_queryset(self):
        return

def index(request):
    return HttpResponse("Hello world")