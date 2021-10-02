
from django.urls import path

from . import views

# do seznamu s adresami vlozim svoje adrese
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("kontakty", views.ContactsView.as_view(), name="contacts"),
    path('onas', views.OnasView.as_view(), name="onas"),
    path('kurzy', views.CourseListView.as_view(), name="course_list"),
    path("branch", views.BranchListView.as_view(), name="branch"),
    path("lide", views.PeopleListView.as_view(), name="people"),
    path('kurz/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path("branch/<int:pk>", views.BranchDetailView.as_view(), name="branch_detail"),



]
