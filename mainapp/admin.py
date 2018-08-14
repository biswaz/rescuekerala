from django.contrib import admin
from .models import Request, Volunteer, Contributor, DistrictNeed, DistrictCollection

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('dateadded',)

admin.site.register(Request, RequestAdmin)
admin.site.register(Volunteer)
admin.site.register(Contributor)
admin.site.register(DistrictNeed)
admin.site.register(DistrictCollection)
