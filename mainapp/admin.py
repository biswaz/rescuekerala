from django.contrib import admin
from .models import Request, Volunteer, Contributor, DistrictNeed, DistrictCollection, DistrictManager


class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('dateadded',)
    ordering = ('district',)


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'organisation',)
    list_filter = ('district', )

admin.site.register(Request, RequestAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Contributor)
admin.site.register(DistrictNeed)
admin.site.register(DistrictCollection)
admin.site.register(DistrictManager)
