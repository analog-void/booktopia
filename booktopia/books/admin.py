from booktopia.books.models import Book, Author, Editions, RentHistory, StatusHistory, Reviews, Comments
from booktopia.common.admin_common_fields import book_common_fields
from booktopia.common.admin_settings import *


# admin.TabularInline
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'editions',
                    'owner', 'book_current_status', 'visual_condition')
    ordering = ('name',)
    search_fields = ('name', 'author_name', 'editions',)

    list_filter = ('name', 'editions',
                   'visual_condition', 'book_to_read_by_owner',
                   'book_current_status',)

    fieldsets = book_common_fields
    readonly_fields = ('record_created_at', 'record_updated_at', 'image_cover_front', 'image_cover_back')

    allow_add = True


class AuthorInline(admin.StackedInline):
    model = Book
    extra = 0
    classes = ['collapse']
    fieldsets = book_common_fields

    allow_add = True


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        AuthorInline,
    ]

    fieldsets = ('Данни Автор', {
        'fields': (('first_name', 'last_name',),
                   ('pseudonym', 'nationality'),
                   ('date_of_birth', 'date_of_death'),)
    }),
    # readonly_fields = ('record_created_at', 'record_updated_at')


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

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
# admin.site.register(Comments, CommentAdmin)
admin.site.register(Comments)

admin.site.register(Editions)
admin.site.register(RentHistory)
admin.site.register(StatusHistory)
admin.site.register(Reviews)

