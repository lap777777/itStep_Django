from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
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

class ApplicationCreateView(CreateView):
    template_name = "application_create.html"
    model = models.Application
    fields = ["first_name", "last_name", "email", "course"]
    success_url = reverse_lazy("application_confirmation")
  
class ApplicationCreateView1(CreateView):
    template_name = "application_create1.html"
    model = models.Application
    fields = ["first_name", "last_name", "email", "course"]
    success_url = reverse_lazy("application_confirmation")
    def from_valid(self, form):
        course_id = self.kwargs["pk"]
        course = models.Course.object.get(pk=course_id)
        form.instance.course = course
        return super().form_valid(form)

class ApplicationConfirmation(TemplateView):
    template_name = "application_confirmation.html"

class RegisterCreateView(CreateView):
    template_name = "registration.html"
    model = models.Registration
    fields = ["name", "surname", "email", "birth"]
    success_url = reverse_lazy("registration_confirmation")

class RegistrationConfirmation(TemplateView):
    template_name = "registration_confirmation.html"

class ApplicationsListView(ListView):
    template_name = "application_list.html"
    model = models.Application
    def get_queryset(self):
        cislo_kurzu = self.kwargs['pk']
        query_set = models.Application.objects.filter(course_id=cislo_kurzu)
        return query_set
    # get_query nastavuje odkud bude brat object data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cislo_kurzu"] = models.Course.objects.get(pk=self.kwargs['pk'])
        return context

class BranchApplicationListView(ListView):
    template_name = "branch_application_list.html"
    model = models.Course
    def get_queryset(self):
        cislo_pobocky = self.kwargs['pk']
        query_set = models.Course.objects.filter(branch_id=cislo_pobocky)
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cislo_pobocky"] = models.Branch.objects.get(pk=self.kwargs['pk'])
        return context
