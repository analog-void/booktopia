from booktopia.common.admin_settings import *
from .models import Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'family_name', 'date_of_birth', 'email', 'mobile_phone')
    ordering = ('family_name', 'first_name')
    list_filter = ('gender',)

    fieldsets = ('Данни Собственик', {
        'fields': (('first_name', 'middle_name',),
                   ('family_name', 'gender', 'date_of_birth',),
                   ('email', 'mobile_phone',),
                   'photo',
                   ('record_created_at', 'record_updated_at',),
                   )}),
    readonly_fields = ('record_created_at', 'record_updated_at',)







class OwnerInline(admin.StackedInline):
    model = Owner
    extra = 0
    classes = ['collapse']
    # fieldsets = book_common_fields

    allow_add = True


admin.site.register(Owner, OwnerAdmin)
