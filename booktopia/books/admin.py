from booktopia.books.models import Book, Author, Editions, StatusHistory, Comments, CommentsAuthors, \
    CommentsEditions
from booktopia.common.admin_common_fields import book_common_fields, author_common_fields
from booktopia.common.admin_settings import *


class AuthorInline(admin.StackedInline):
    model = Author
    extra = 0
    # classes = ['collapse']
    fieldsets = author_common_fields
    allow_add = True
    # allow_add = False


class BookInline(admin.StackedInline):
    model = Book
    extra = 0
    classes = ['collapse']
    fieldsets = book_common_fields
    allow_add = True


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'pseudonym',
                    'date_of_birth',
                    'nationality',)

    ordering = ('last_name',)
    search_fields = ('last_name', 'pseudonym')
    list_filter = ('first_name', 'last_name', 'nationality',)

    allow_add = True

    # inlines = [
    #     BookInline
    # ]


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'editions',
                    'user', 'book_current_status', 'visual_condition')
    ordering = ('name',)
    search_fields = ('name', 'editions',)  # 'author_name'

    list_filter = ('name', 'editions',
                   'visual_condition', 'book_to_read_by_owner',
                   'book_current_status',)

    fieldsets = book_common_fields
    readonly_fields = ('record_created_at', 'record_updated_at', 'image_cover_front', 'image_cover_back')

    allow_add = True

    # inlines = [
    #     AuthorInline
    # ]


class EditionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
        'stars')

    ordering = ('name',)
    search_fields = ('name', 'country',)
    list_filter = ('name', 'country')



class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'book_id',
                    'record_created_at',
                    'record_updated_at')

    ordering = ('user_id',
                'book_id',)

    search_fields = ('user_id',
                     'book_id',)

    list_filter = ('user_id',
                   'book_id',)


class AuthorsCommentsAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'author_id',
                    'record_created_at',
                    'record_updated_at')

    ordering = ('user_id',
                'author_id',)

    search_fields = ('user_id',
                     'author_id',)

    list_filter = ('user_id',
                   'author_id',)


class EditionsCommentsAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'edition_id',
                    'record_created_at',
                    'record_updated_at')

    ordering = ('user_id',
                'edition_id',)

    search_fields = ('user_id',
                     'edition_id',)

    list_filter = ('user_id',
                   'edition_id',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

admin.site.register(Editions, EditionsAdmin)
admin.site.register(StatusHistory)

admin.site.register(Comments, CommentsAdmin)
admin.site.register(CommentsAuthors, AuthorsCommentsAdmin)
admin.site.register(CommentsEditions, EditionsCommentsAdmin)

"""
class UserAdmin(admin.StackedInline):
    model = User
class ContactAdmin(admin.StackedInline):
    model = Contact

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [ UserAdmin, ContactAdmin ]
"""

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         AuthorInline, BookInline
#     ]
#
#     fieldsets = ('Данни Автор', {
#         'fields': (('first_name', 'last_name',),
#                    ('pseudonym', 'nationality'),
#                    ('date_of_birth', 'date_of_death'),)
#     }),
#     # readonly_fields = ('record_created_at', 'record_updated_at')


#################

"""
class CommentInline(admin.StackedInline):
    model = Book
    extra = 0
    classes = ['collapse']
    fieldsets = book_common_fields

    allow_add = True


class CommentAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

    fieldsets = book_comment_fields

    #### readonly_fields = ('record_created_at', 'record_updated_at')
"""
