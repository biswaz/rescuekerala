from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('request/', views.CreateRequest.as_view(), name='requestview'),
    path('volunteer/', views.RegisterVolunteer.as_view(), name='registerview'),
    path('requests/', views.request_list, name='requestlistview'),
    path('volunteers/', views.volunteer_list, name='volunteerlistview'),
    path('reg_success/', views.RegSuccess.as_view(), name='reg_successview'),
    path('req_sucess/', views.ReqSuccess.as_view(), name='req_sucessview'),
    path('district_needs/', views.DistNeeds.as_view(), name='distneedsview'),
]
