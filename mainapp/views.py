from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Request


class CreateRequest(CreateView):
    model = Request
    template_name='mainapp/request_form.html'
    fields = ['district', 'location', 'requestee', 'requestee_phone', 'needwater', 'needfood', 'needcloth', 'needmed', 'needothers',]
    success_url = '/submitted'

def submittedview(request):
    return HttpResponse('submitted :)')
