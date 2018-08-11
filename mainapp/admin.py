from django.contrib import admin
from .models import Request, Volunteer

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('dateadded',)

admin.site.register(Request, RequestAdmin)
admin.site.register(Volunteer)
