from django.contrib import admin
from .models import Car, Insurance, Tax, TechnicalCheckIn, Service


class CarAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'firm',
                    'power',
                    'cylinder',
                    'fuel_consumption',
                    'fuel_type',
                    'registration_number',
                    'chassis']


admin.site.register(Car, CarAdmin)


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['insurance_company',
                    'vehicle',
                    'policy_number',
                    'activation_date',
                    'expiration_date',
                    'prime']


admin.site.register(Insurance, InsuranceAdmin)


class TaxAdmin(admin.ModelAdmin):
    list_display = ['vehicle',
                    'tax_amount',
                    'date_of_tax_payment',
                    'next_due_date',]


admin.site.register(Tax, TaxAdmin)


class TechnicalCheckInAdmin(admin.ModelAdmin):
    list_display = ['vehicle',
                    'check_in_number',
                    'comment',
                    'date_of_checkIn',
                    'date_of_next_checkIn',
                    'cost_of_checkIn']


admin.site.register(TechnicalCheckIn, TechnicalCheckInAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['vehicle',
                    'service_supplier',
                    'order_id',
                    'category',
                    'date_of_service',
                    'next_date',
                    'cost_of_service',
                    'cost_of_parts']


admin.site.register(Service, ServiceAdmin)




