from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('request/', views.CreateRequest.as_view(), name='requestview'),
    path('volunteer/', views.RegisterVolunteer.as_view(), name='registerview'),
    path('requests/', views.request_list, name='requestlistview'),
    path('volunteers/', views.volunteer_list, name='volunteerlistview'),
    path('submitted/', views.submittedview, name='submittedview'),
]
