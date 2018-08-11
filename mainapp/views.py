from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Request, Volunteer
import django_filters

class CreateRequest(CreateView):
    model = Request
    template_name='mainapp/request_form.html'
    fields = ['district', 'location', 'requestee', 'requestee_phone', 'needwater', 'needfood', 'needcloth', 'needmed', 'needkit_util', 'needtoilet', 'needothers',]
    success_url = '/'

class RegisterVolunteer(CreateView):
    model = Volunteer
    fields = ['name', 'phone', 'organisation', 'address',]
    success_url = '/'


class HomePageView(TemplateView):
    template_name = "home.html"


def submittedview(request):
    return HttpResponse('submitted :)')


class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = Request
        # fields = ['district', 'status', 'needwater', 'needfood', 'needcloth', 'needmed', 'needkit_util', 'needtoilet', 'needothers',]
        fields = ['district', 'status']

def request_list(request):
    filter = RequestFilter(request.GET, queryset=Request.objects.all())
    return render(request, 'mainapp/request_list.html', {'filter': filter})


class VolunteerFilter(django_filters.FilterSet):
    class Meta:
        model = Volunteer
        fields = ['district']

def volunteer_list(request):
    filter = VolunteerFilter(request.GET, queryset=Volunteer.objects.filter(is_spoc=True))
    return render(request, 'mainapp/volunteer_list.html', {'filter': filter})
