from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page that lists courses
    path('courses/', views.course_list, name='course_list'),  # Course list page
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),  # Course detail page
]
