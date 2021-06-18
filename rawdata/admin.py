from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.



class RawdataAdmin(ImportExportModelAdmin):
    list_display = ['pk','content','note','priority','number','translation_eng']
    list_display_links = ['content','number']
    search_fields = ['pk','content']
    list_filter = ['note','priority']

    class Meta:
        model = Rawdata

admin.site.register(Rawdata,RawdataAdmin)
