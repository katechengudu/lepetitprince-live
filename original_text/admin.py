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
    chapter_title = fields.Field(
        column_name='chapter_title',
        attribute='chapter_title',
        widget=ForeignKeyWidget(Chapter, 'title_name'))
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


admin.site.register(Book,BookAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Sentence,SentenceAdmin)


