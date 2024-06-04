from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class Index(TemplateView):
    template_name='index.html'

class FormQuetions(TemplateView):
    template_name = 'form-repeater.html'

class FormQuiz(TemplateView):
    template_name="form-repeater.html"