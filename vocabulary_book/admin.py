from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

from original_text.models import Token
from django.contrib.auth.models import User


class MyWordResource(resources.ModelResource):
    token_id = fields.Field(
        column_name='token_id',
        attribute='token_id',
        widget=ForeignKeyWidget(Token, 'pk'))
    user_id = fields.Field(
        column_name='user_id',
        attribute='user_id',
        widget=ForeignKeyWidget(User, 'pk'))
    related_token_id = fields.Field(
        column_name='related_token_id',
        attribute='related_token_id',
        widget=ForeignKeyWidget(Token, 'pk'))
    class Meta:
        model = MyWord

class MyWordAdmin(ImportExportModelAdmin):
    list_display = ['pk','mynote4review']
    list_display_links = ['mynote4review']
    search_fields = ['pk','mynote4review','token_id']
    list_filter = ['timestamp','user_id']
    resource_class = MyWordResource
    class Meta:
        model = MyWord

admin.site.register(MyWord,MyWordAdmin)

