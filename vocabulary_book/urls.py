from django.urls import path, re_path
from .views import *


app_name = "vocabulary_book"
urlpatterns = [
    path('my_vocabulary/', MyWordView.as_view(),name='my_vocabulary'),

]
