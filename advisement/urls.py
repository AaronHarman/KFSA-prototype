from django.urls import path

from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='adv_home'),
    path('student_overview/<int:advisee>/', views.advisee_overview, name="overview"),
    path('add_advisement/<int:advisee>/', views.add_advisement, name="add_advisement"),
    path('edit_advisement/<int:advisement>', views.edit_advisement, name="edit_advisement"),
    path('view_advisement/<int:advisement>', views.view_advisement, name="view_advisement"),


    path('checksheets/', views.checksheet_listing, name="list_checksheets"),
    path('add_checksheet/', views.add_checksheet, name="add_checksheet"),
    path('add_students/', views.add_students, name="add_students"),
    path('advisee_list/', views.advisee_list, name="advisee_list"),
    path('edit_advisee/<int:advisee>', views.edit_advisee, name="edit_advisee"),
]


