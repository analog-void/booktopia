from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = "BookTopia - Зона за Администрация"
admin.site.site_title = "BookTopia - Зона за Администрация"
admin.site.index_title = "Добре дошли в BookTopia!"

GRAPPELLI_AUTOCOMPLETE_LIMIT = 10

# removing groups, no real use
admin.site.unregister(Group)
