from booktopia.books.models import Book, Author, Editions, RentHistory, StatusHistory, Comments
from booktopia.common.admin_common_fields import book_common_fields, author_common_fields
from booktopia.common.admin_settings import *

# admin.TabularInline

# class AuthorInline(admin.StackedInline):
#     model = Author
#     extra = 0
#     # classes = ['collapse']
#     fieldsets = author_common_fields
#
#     # allow_add = True
#     allow_add = False


class BookAdmin(admin.ModelAdmin):
    list_display = ('name',  'editions',
                    'user', 'book_current_status', 'visual_condition')
    ordering = ('name',)
    search_fields = ('name', 'editions',) #'author_name'

    list_filter = ('name', 'editions',
                   'visual_condition', 'book_to_read_by_owner',
                   'book_current_status',)

    fieldsets = book_common_fields
    readonly_fields = ('record_created_at', 'record_updated_at', 'image_cover_front', 'image_cover_back')

    allow_add = True

    # inlines = [
    #     AuthorInline
    # ]


"""
class UserAdmin(admin.StackedInline):
    model = User
class ContactAdmin(admin.StackedInline):
    model = Contact

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [ UserAdmin, ContactAdmin ]
"""


class BookInline(admin.StackedInline):
    model = Author
    extra = 0
    classes = ['collapse']
    fieldsets = book_common_fields

    allow_add = True


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
# FIXME: Comment admin
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

admin.site.register(Author)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
# admin.site.register(Comments, CommentAdmin)
admin.site.register(Comments)

admin.site.register(Editions)
# admin.site.register(RentHistory)
admin.site.register(StatusHistory)
# admin.site.register(Reviews)

