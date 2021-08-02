from django.contrib.auth import get_user_model
from django.db import models

from booktopia.books.models import Book
# from booktopia.books.models import Book

UserModel = get_user_model()


# class Comments(models.Model):
#     # timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата на създаване на записа')
#     user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     book_id = models.ManyToManyField(Book, on_delete=models.CASCADE)
#
#     # user_id_num = models.IntegerField(default=0)
#     # book_id_num = models.IntegerField(unique=True, blank=True)
#
#     comment = models.TextField(verbose_name='Съдържание на кометара', null=True)
#
#     # TODO: A les sortir dans un modele ou app separee
#     up_votes_count = models.PositiveSmallIntegerField(default=0)
#     down_votes_count = models.PositiveSmallIntegerField(default=0)
#
#     # record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
#     #                                          null=True, verbose_name='Дата на създаване на записа')
#     # record_updated_at = models.DateTimeField(auto_now=True, blank=True,
#     #                                          null=True, verbose_name='Дата на промяна на записа')
#
#     # def __str__(self):
#     #     return str(self.timestamp)
#
#     class Meta:
#         verbose_name = 'Коментар'
#         verbose_name_plural = 'Коментари'
