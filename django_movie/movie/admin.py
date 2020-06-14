from django.contrib import admin

# Register your models here.
from .models import  Category, Actor, Ganre, Movie, RatingStar, Rating, Reviews, MovieShots 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    # Указаное имя в данной строке становиться ссылкой
    list_display_links =("name",)



class ReviewInline(admin.StackedInline):
    model = Reviews
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    # Это строка выводит окно поиска по указанным элементам
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    #Это поле добовляет кнопки в верху страницы
    save_on_top = True
    #Добовляет кнопку сохранить как новый обЪект
    save_as = True
    # Это поле делает указанный атрибут редактируемым
    list_editable = ("draft",)
    #fields = (("actors", "directors", "genres"),)
    fieldsets = (
            (None,{
                "fields":(("title", "tagline"),)
                }),
            (None,{
                "fields":("description", "poster")
                }),
            (None,{
                "fields":(("year", "world_premiere", "country"),)
                }),
            ("Actors", {
                "classes": ("collapse",),
                "fields":(("actors", "directors", "genres", "category"),)
                }),
            (None,{
                "fields":(("budget", "fees_in_usa", "fees_in_world", ),)
                }),
            ("Options", {
                "fields":(("url", "draft"),)
                }),
    )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "movie",)
    #Это поле запрещает редактирование данных полей 
    #readonly_fields = ("name", "email")

@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "image")
    search_fields = ("name", "age")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "ip")

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie")


admin.site.register(RatingStar)
