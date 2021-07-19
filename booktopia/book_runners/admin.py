from django.contrib import admin

from .models import RunnerLog, RunnerCompany


class RunnerLogAdmin(admin.ModelAdmin):
    # list_display = ()
    fieldsets = ('Данни Автор', {
        'fields': (('transportation_type', 'runner_id',),
                   ('from_place', 'ts_pickup',),
                   ('to_place', 'ts_delivery'),
                   'delivery_rating', 'comment',)
    }),


admin.site.register(RunnerLog, RunnerLogAdmin)
admin.site.register(RunnerCompany)
