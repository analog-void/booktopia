book_common_fields = (
    ('Обща информация', {
        'fields': (('name','author_name'),
                   'release_year',
                   ('user', 'book_current_status'),
                   ('price_for_rent', 'price_for_sell'),
                   ('is_for_sale', 'is_sold', 'is_lost',),
                   ('is_hidden', 'is_archived'))
    }),

    ('Текущо издание', {
        'fields': ('editions', ('series', 'pages_count'))
    }),

    ('Преводи', {
        'fields': (('translated', 'original_name', 'release_number'), ('edition_lang', 'edition_lang_orig',))
    }),

    ('Общо състояние', {
        'fields': ('visual_condition', ('measure_x', 'measure_y', 'weight_grams'))
    }),

    ('Каталожна информация', {
        'fields': ('catalog_num', ('isbn_code', 'oclc_code',))
    }),

    ('Оценка', {
        'fields': ('synopsis', 'notes', 'book_reviews',)
    }),

    ('Медия', {
        'fields': (
            'cover_front',
            # FIXME: A voir pourquoi le truc plante
            'image_cover_front',
            'cover_back',
            'image_cover_back',
            'generated_qr_code_image',
            'tags',)
    }),

    ('Други', {
        'classes': ('grp-collapse grp-closed',),
        # 'classes': ('collapse',), # Pour la template d'origine
        'fields': ('book_to_read_by_owner', 'book_reserved',
                   ('has_been_rented_times', 'generated_qr_code_content'),
                   ('book_rent_history', 'book_transportation_history'),

                   # FIXME: Timestams in ADMIN bug ....
                   # ('record_created_at', 'record_updated_at'),
                   )
    }))

# FIXME: Comments
# book_comment_fields = (
#     ('Коментар', {
#         'fields': (('user_id', 'book_id'),
#                    'comment',
#                    ('up_votes_count', 'down_votes_count'),
#                    # 'timestamp',
#                    )
#     }),
# )

# owner_common_fields = ()

author_common_fields = (
    ('Автор', {
        'fields': (
            'book_id',
            ('first_name', 'last_name'),
            'pseudonym',
            ('date_of_birth', 'date_of_death'),
            ('nationality', 'wiki_page')
        )
    }),
)
