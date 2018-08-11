from django.urls import path

from . import views

urlpatterns = [
    path('request/', views.CreateRequest.as_view(), name='requestview'),
    path('submitted/', views.submittedview, name='submittedview'),
]
