from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path("<int:course_id>/", views.create_checkout_session, name="create_checkout_session"), 
    path("course_success/<int:course_id>/", views.course_success, name="course_success"),
    path("course_cancel/", views.course_cancel, name="course_cancel"),  # Added missing slash and corrected function
    path("stripe/webhook/", views.stripe_webhook, name="stripe_webhook"),  # Added missing slash
]
