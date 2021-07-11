from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class BookAdmin(ImportExportModelAdmin):
    list_display = ['title','author','pk','note']
    list_display_links = ['title','author']
    search_fields = ['title']
    class Meta:
        model = Book


class ChapterResource(resources.ModelResource):
    book_title = fields.Field(
        column_name='book_title',
        attribute='book_title',
        widget=ForeignKeyWidget(Book, 'title'))
    class Meta:
        model = Chapter

class ChapterAdmin(ImportExportModelAdmin):
    list_display = ['title_name','title_number','pk','note']
    list_display_links = ['title_name']
    search_fields = ['title_name']
    resource_class = ChapterResource
    class Meta:
        model = Chapter

class SentenceResource(resources.ModelResource):
    chapter_id = fields.Field(
        column_name='chapter_id',
        attribute='chapter_id',
        widget=ForeignKeyWidget(Chapter, 'title_name'))
    book_id = fields.Field(
        column_name='book_id',
        attribute='book_id',
        widget=ForeignKeyWidget(Book, 'title'))
    class Meta:
        model = Sentence

class SentenceAdmin(ImportExportModelAdmin):
    list_display = ['pk','content','note','priority','number','translation_eng']
    list_display_links = ['content','number']
    search_fields = ['pk','content']
    list_filter = ['note','priority']
    resource_class = SentenceResource
    class Meta:
        model = Sentence


class LemmaAdmin(ImportExportModelAdmin):
    list_display = ['pk','text']
    list_display_links = ['text']
    search_fields = ['pk','text']
    list_filter = ['note','priority']
    class Meta:
        model = Lemma


class TokenResource(resources.ModelResource):
    sentence_id = fields.Field(
        column_name='sentence_id',
        attribute='sentence_id',
        widget=ForeignKeyWidget(Sentence, 'pk'))
    token_lemma = fields.Field(
        column_name='token_lemma',
        attribute='token_lemma',
        widget=ForeignKeyWidget(Lemma, 'text'))
    class Meta:
        model = Token

class TokenAdmin(ImportExportModelAdmin):
    list_display = ['pk','text','pos','tag','dep','note']
    list_display_links = ['text']
    search_fields = ['pk','text']
    list_filter = ['note','priority']
    resource_class = TokenResource
    class Meta:
        model = Token


admin.site.register(Book,BookAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Sentence,SentenceAdmin)
admin.site.register(Lemma,LemmaAdmin)
admin.site.register(Token,TokenAdmin)

