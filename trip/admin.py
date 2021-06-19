from django.contrib import admin
from .models import Organization, Employee, Mission, Fuel, Incident


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'address']


admin.site.register(Organization, OrganizationAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'organisation',
                    'role',
                    'is_tms_manager']


admin.site.register(Employee, EmployeeAdmin)


class MissionAdmin(admin.ModelAdmin):
    list_display = ['reference',
                    'driver',
                    'vehicle',
                    'is_permanent',
                    'start_date',
                    'end_date',
                    'odometer_initial_index',
                    'odometer_final_index']


admin.site.register(Mission, MissionAdmin)


class FuelAdmin(admin.ModelAdmin):
    list_display = ['quantity',
                    'cost',
                    'date',
                    'odometer_index',
                    'mission']


admin.site.register(Fuel, FuelAdmin)


class IncidentAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'date',
                    'mission']


admin.site.register(Incident, IncidentAdmin)
