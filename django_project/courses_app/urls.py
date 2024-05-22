from django.urls import path
from . import views

urlpatterns = [
    path('courses_page/', views.courses_page, name="courses_page"),
]