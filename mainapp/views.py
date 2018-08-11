from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Request, Volunteer


class CreateRequest(CreateView):
    model = Request
    template_name='mainapp/request_form.html'
    fields = ['district', 'location', 'requestee', 'requestee_phone', 'needwater', 'needfood', 'needcloth', 'needmed', 'needkit_util', 'needtoilet', 'needothers',]
    success_url = '/submitted'

class RegisterVolunteer(CreateView):
    model = Volunteer
    fields = ['name', 'phone', 'organisation', 'address',]

class HomePageView(TemplateView):
    template_name = "home.html"


def submittedview(request):
    return HttpResponse('submitted :)')
