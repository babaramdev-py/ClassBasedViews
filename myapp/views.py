from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView, DetailView
from myapp import models
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    # Learn how to use Kwargs and Args

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Injected.'
        return context
    

class SchoolListView(ListView):
    def __init__(self):
        print("List was called!")
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    def __init__(self):
        print("I was called")
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'myapp/school_detail.html'