from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import  Category, Actor, Ganre, Movie, RatingStar, Rating, Reviews, MovieShots
from django import forms
from ckeditor_uploader.widgets  import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


""" Редактор """
class MovieAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'




@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    # Указаное имя в данной строке становиться ссылкой
    list_display_links =("name",)
    prepopulated_fields = {"url":("name",)}



class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    # Функыця отоброжения картинок в админке
    def get_image(self, odj):
        return mark_safe(f'<img src={odj.image.url} widht="50" height="60"')
    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    prepopulated_fields = {"url":("title",)}
    # Это строка выводит окно поиска по указанным элементам
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline]
    #Это поле добовляет кнопки в верху страницы
    save_on_top = True
    #Добовляет кнопку сохранить как новый обЪект
    save_as = True
    # Это поле делает указанный атрибут редактируемым
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    #Редактор
    form = MovieAdminForm
    readonly_fields = ("get_image",)
    #fields = (("actors", "directors", "genres"),)
    fieldsets = (
            (None,{
                "fields":(("title", "tagline"),)
                }),
            (None,{
                "fields":("description", ("poster", "get_image"))
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


    def get_image(self, odj):
        """Функцыя показа изображения"""
        return mark_safe(f'<img src={odj.poster.url} widht="100" height="110"')


    def unpublish(self, request, queryset):
        """Снять с публикации"""

        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = " 1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей бли обновленны"
        self.message_user(request,f"{message_bit}")


    def publish(self, request, queryset):
           """Опубликовать"""
           row_update = queryset.update(draft=False)
           if row_update == 1:
               message_bit = " 1 запись была обновлена"
           else:
               message_bit = f"{row_update} записей бли обновленны"
               self.message_user(request,f"{message_bit}")


    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Снять с публикацыи"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Постер"




@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "movie",)
    #Это поле запрещает редактирование данных полей
    #readonly_fields = ("name", "email")

@admin.register(Ganre)
class GanreAdmin(TranslationAdmin):
    list_display = ("name", "url")
    prepopulated_fields = {"url":("name",)}

@admin.register(Actor)
class ActorAdmin(TranslationAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)
    # Функыця отоброжения картинок в админке
    def get_image(self, odj):
        return mark_safe(f'<img src={odj.image.url} widht="50" height="60"')
    get_image.short_description = "Изображение"
    search_fields = ("name", "age")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")

@admin.register(MovieShots)
class MovieShotsAdmin(TranslationAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)


    # Функыця отоброжения картинок в админке
    def get_image(self, odj):
        return mark_safe(f'<img src={odj.image.url} widht="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)


"""Заголовок в админке"""
admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'
