from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import UpdateView
from main import models
# Create your views here

class Index(View):
    def get(self, request):
        return HttpResponse("GET request")

    def post(self, request):
        return HttpResponse("POST response")

#GENERIC VIEWS--> Detail View for info
#List View 
#Create View 
#Update View 
#Delete View  

class CollegeDetail(DetailView):
    model=models.College  #only mandatory field, does not require meta
    template_name= 'college_detail.html'

class CollegeList(ListView):
    model = models.College
    template_name = 'college_list.html'
    context_object_name='colleges'

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'

class studentCreate(CreateView):
    model = models.Student
    template_name = 'student_create.html'
    fields = '__all__'
    success_url = '/college'

class CollegeUpdate(UpdateView):
    model = models.College
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'

class StudentDelete(DeleteView):
    model = models.Student
    template_name = 'confirm.html'
    success_url = '/college'
