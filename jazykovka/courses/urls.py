
from django.urls import path

from . import views

# do seznamu s adresami vlozim svoje adrese
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("kontakty", views.ContactsView.as_view(), name="contacts"),
    path('onas', views.OnasView.as_view(), name="onas"),
    path('kurzy', views.CourseListView.as_view(), name="course_list"),
    path("pobocka", views.BranchListView.as_view(), name="branch"),
    path("lide", views.PeopleListView.as_view(), name="people"),
    path('kurz/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path("pobocka/<int:pk>", views.BranchDetailView.as_view(), name="branch_detail"),
    path("application", views.ApplicationCreateView.as_view(), name="application_create"),
    path("prihlaska/<int:pk>", views.ApplicationCreateView1.as_view(), name="application_create1"),
    path("prihlaska/potvrzeni", views.ApplicationConfirmation.as_view(), name="application_confirmation"),
    path("registrace", views.RegisterCreateView.as_view(), name="registration"),
    path("registrace/potvrzeni", views.RegistrationConfirmation.as_view(), name="registration_confirmation"),
    path('kurz/<int:pk>/applications', views.ApplicationsListView.as_view(), name='application_list'),
    path("pobocka/<int:pk>/applications", views.BranchApplicationListView.as_view(), name="branch_application_list"),


]
