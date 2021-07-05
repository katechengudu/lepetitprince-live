from django.urls import path
from .views import *


app_name = "original_text"
urlpatterns = [
    path('', BookView.as_view(),name='book'),
    path('book/sentence_grammar/<int:pk>', Sentence_GrammarView.as_view(),name='Sentence_Grammar'),
    path('book/<int:pk>', SentenceView.as_view(),name='sentence'),
    path('search/',SearchView.as_view(),name='search'),
]
