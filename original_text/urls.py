from django.urls import path
from .views import *


app_name = "original_text"
urlpatterns = [
    path('', SentenceView.as_view(),name='sentence'),
    path('search/',SearchView.as_view(),name='search'),
    # path('sentence-chunks/<int:pk>',Sentence_ChunksView.as_view(),name='sentence-chunks'),
]
