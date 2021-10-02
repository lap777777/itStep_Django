from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"

class OnasView(TemplateView):
    template_name = "onas.html"

class CourseListView(ListView):
    template_name = "course_list.html"
    model = models.Course

class BranchListView(ListView):
    template_name = "branch.html"
    model = models.Branch

class PeopleListView(ListView):
    template_name = "people.html"
    model = models.Person

class CourseDetailView(DetailView):
    template_name = "course_detail.html"
    model = models.Course

class BranchDetailView(DetailView):
    template_name = "branch_detail.html"
    model = models.Branch

