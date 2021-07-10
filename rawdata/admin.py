from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class SourceAdmin(ImportExportModelAdmin):
    list_display = ['title','pk','note']
    list_display_links = ['title']
    search_fields = ['title']
    class Meta:
        model = Source

class RawdataAdmin(ImportExportModelAdmin):
    list_display = ['pk','content','note','priority','translation_eng']
    list_display_links = ['content']
    search_fields = ['pk','content']
    list_filter = ['note','priority']
    class Meta:
        model = Rawdata



class NLP_token_RawdataAdmin(ImportExportModelAdmin):
    list_display = ['pk','note','nlp_text','nlp_pos']
    list_display_links = ['nlp_text']
    search_fields = ['pk','nlp_text']
    list_filter = ['note','nlp_pos']
    class Meta:
        model = NLP_token_Rawdata


class LemmaAdmin(ImportExportModelAdmin):
    list_display = ['pk','text']
    list_display_links = ['text']
    search_fields = ['pk','text']
    list_filter = ['note','priority']
    class Meta:
        model = Lemma


admin.site.register(Source,SourceAdmin)
admin.site.register(Rawdata,RawdataAdmin)
admin.site.register(NLP_token_Rawdata,NLP_token_RawdataAdmin)
admin.site.register(Lemma,LemmaAdmin)
