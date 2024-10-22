from django.contrib import admin
from django.urls import path, include
from course import views as course_views  # Import course_views from the course app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("payment/", include("payment.urls")),
    path("course/", include("course.urls")),
    path('', course_views.home, name='home'),  # Now course_views.home is correctly referenced
]