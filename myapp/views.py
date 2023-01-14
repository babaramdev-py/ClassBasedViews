from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from myapp import models
from django.urls import reverse, reverse_lazy
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

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')

class SchoolUpdateView(UpdateView):
    fields = ('principal','name')
    model= models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("myapp:list")