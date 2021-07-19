# @property
# def image_cover_front(self):
#     return mark_safe('<img src="{}" width="200" height="300" />'.format(self.book_cover_front.url))
#
# @property
# def image_cover_back(self):
#     return mark_safe('<img src="{}" width="480" height="640" />'.format(self.book_cover_back.url))


# class BookRating():
#     pass
#
#
# class Tags():
#     pass
#
#
# class Similars():
#     # book_rating - somme de tous les votes, par des utilisateurs
#     # par le meme auteur ... par le meme edition
#     # par le meme ... d'autres criteres
#     pass

#
#     def __str__(self):
#         return "{n} x {child} to make {parent}".format(
#             parent=self.part.full_name,
#             child=self.sub_part.full_name,
#             n=helpers.decimal2string(self.quantity))
#
#     def available_stock(self):
#         """
#         Return the available stock items for the referenced sub_part
#         """
#
#         query = self.sub_part.stock_items.all()
#
#         query = query.prefetch_related([
#             'sub_part__stock_items',
#         ])
#
#         query = query.filter(StockModels.StockItem.IN_STOCK_FILTER).aggregate(
#             available=Coalesce(Sum('quantity'), 0)
#         )
#
#         return query['available']
#
#     def get_overage_quantity(self, quantity):
#         """ Calculate overage quantity
#         """
#
#         # Most of the time overage string will be empty
#         if len(self.overage) == 0:
#             return 0
#
#         overage = str(self.overage).strip()
#
#         # Is the overage a numerical value?
#         try:
#             ovg = float(overage)
#
#             if ovg < 0:
#                 ovg = 0
#
#             return ovg
#         except ValueError:
#             pass
#
#         # Is the overage a percentage?
#         if overage.endswith('%'):
#             overage = overage[:-1].strip()
#
#             try:
#                 percent = float(overage) / 100.0
#                 if percent > 1:
#                     percent = 1
#                 if percent < 0:
#                     percent = 0
#
#                 # Must be represented as a decimal
#                 percent = Decimal(percent)
#
#                 return float(percent * quantity)
#
#             except ValueError:
#                 pass
#
#         # Default = No overage
#         return 0
#
#     def get_required_quantity(self, build_quantity):
#         """ Calculate the required part quantity, based on the supplier build_quantity.
#         Includes overage estimate in the returned value.
#
#         Args:
#             build_quantity: Number of parts to build
#
#         Returns:
#             Quantity required for this build (including overage)
#         """
#
#         # Base quantity requirement
#         base_quantity = self.quantity * build_quantity
#
#         # Overage requiremet
#         ovrg_quantity = self.get_overage_quantity(base_quantity)
#
#         required = float(base_quantity) + float(ovrg_quantity)
#
#         return required
#
#     @property
#     def price_range(self):
#         """ Return the price-range for this BOM item. """
#
#         prange = self.sub_part.get_price_range(self.quantity)
#
#         if prange is None:
#             return prange
#
#         pmin, pmax = prange
#
#         if pmin == pmax:
#             return decimal2string(pmin)
#
#         # Convert to better string representation
#         pmin = decimal2string(pmin)
#         pmax = decimal2string(pmax)
#
#         return "{pmin} to {pmax}".format(pmin=pmin, pmax=pmax)
#



"""
    def upload(instance, filename):
        return "document/" + instance.user.name +"/" + filename

    And in the filefield of model

    upload_to=upload
"""


"""
(В ТЕЗИ ЗА МОЖЕ ДА СЕ ДОБАВЯ ОТ ПОТРЕБИТЕЛЯ)
АВТОР
ИЗДАДЕЛСТВО

КОМЕНТАРИ ОТ ВСИЧКИ, НЕ САМО ЧИТАТЕЛИ
КОМЕНТАРИ ОТ ХОРА, КОИТО СА Я ПРОЧЕЛИ (РЕЦЕНЗИИ, РЕЗЮМЕ И ТН)

* BOOK RENT HISTORY
* BOOK TRAVEL HISTORY

BOOK RATING
BOOK TAGS
SIMILARS

charts - top 20, par classement utilisateur
relation avel l'auteur, le statut - son histoire - qui l'a eu, ou est il actuelement
ДРУГИ КНИГИ ОТ АВТОРА

book_current_status

"""

"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["question_text"]}),
        ("Date Information", {"fields": ['pub_date'], "classes": ['collapse']}),

    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)    




class ProductPriceInlineAdminView(admin.TabularInline):
    model = ProductPrice
    extra = 1
    classes = ['collapse']
    fieldsets = (
        ('', {
            'fields': ('price',
                       'currency',
                       'unit',
                       'valid_from',
                       'valid_until',
                       'customer_group')
        }),
    )
    allow_add = True


"""


# class OwnerAdmin(admin.TabularInline):
#     model = Owner
#     extra = 1
#     classes = ['collapse']
#     fieldsets = (
#         ('', {
#             'fields': ('first_name',
#                        'middle_name',
#                        'family_name',
#                        'gender',
#                        'date_of_birth',
#                        'email'
#                        'mobile_phone',
#                        'photo',)
#         }),
#     )
#     allow_add = True


# class OwnerAdmin(admin.TabularInline):
#     model = Owner
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         OwnerAdmin,
#     ]





# IMAGES :
# def cover_front(self, obj):
#     return obj.cover_front
#
# def cover_back(self, obj):
#     return obj.cover_back

# cover_front.short_description = 'Корица'
# cover_front.allow_tags = True
#
# cover_back.short_description = 'Гръб'
# cover_back.allow_tags = True





"""
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="{% url 'all books table ' %}">Portfolio</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">

                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'book index' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Blog</a>
                    </li>
                </ul>
            </div>
        </div>

        <!--<style>
            h1 {
                border: 5px solid red;
                }

            h2 {
                border: 4px dotted blue;
                }
            div {
                border: double;
                }
          </style>
          -->
    </nav>



"""


"""
            <div class="d-flex align-items-center">
                <button type="button" class="btn btn-link px-3 me-2">
                    Login
                </button>

                <button type="button" class="btn btn-primary me-3">
                    Sign up for free
                </button>
                <a class="btn btn-dark px-3"
                   href="https://github.com/mdbootstrap/mdb-ui-kit"
                   role="button">
                    <i class="fab fa-github"></i></a>
            </div>


"""

