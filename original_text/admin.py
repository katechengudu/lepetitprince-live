from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class ChapterAdmin(ImportExportModelAdmin):
    list_display = ['title_name','title_number','pk','note']
    list_display_links = ['title_name']
    search_fields = ['title_name']
    class Meta:
        model = Chapter



class ParagraphResource(resources.ModelResource):
    chapter_title = fields.Field(
        column_name='chapter_title',
        attribute='chapter_title',
        widget=ForeignKeyWidget(Chapter, 'title_name'))
    class Meta:
        model = Paragraph

class ParagraphAdmin(ImportExportModelAdmin):
    list_display = ['pk','content','priority','chapter_title','translation_eng']
    list_display_links = ['content','chapter_title']
    search_fields = ['pk','content']
    list_filter = ['note','priority']
    resource_class = ParagraphResource
    class Meta:
        model = Paragraph


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



admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Paragraph,ParagraphAdmin)
admin.site.register(Sentence,SentenceAdmin)


