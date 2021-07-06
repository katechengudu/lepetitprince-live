from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import *
from django.views.decorators.csrf import csrf_exempt

class MyWordView(ListView):
    template_name = 'vocabulary_book/my_vocabulary_book.html'
    context_object_name = 'results'
    model = MyWord

