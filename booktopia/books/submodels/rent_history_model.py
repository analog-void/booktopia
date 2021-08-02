from django.db import models


class RentHistory(models.Model):
    # timestamp_from = models.DateTimeField(auto_created=True)
    timestamp_to = models.DateField()
    by_user = models.IntegerField()
    # rent_duration = models
    rent_event_comment = models.TextField()
    degradations = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата на създаване на записа')
