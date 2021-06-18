from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import *
from django.views.decorators.csrf import csrf_exempt

class SentenceView(ListView):
    template_name = 'original_text/home.html'
    context_object_name = 'results'
    model = Sentence
    ordering = ['pk']

    def get_queryset(self):
        datas = Sentence.objects.all()
        chapter_titles=Chapter.objects.all()
        results = {'datas':datas,
                   'chapter_titles': chapter_titles,
                   'text_language':['french','english','chinese']
                   }
        return results


class SearchView(ListView):
    template_name = 'original_text/search.html'
    model = Sentence
    context_object_name = 'results'

    @csrf_exempt
    def get_queryset(self):
        q1 = self.request.GET.get("text_story")
        q2 = self.request.GET.get("chapter_name")
        q3 = self.request.GET.get("text_language")

        chapter_titles = Chapter.objects.all()

        if q1 or q2 or q3:
            if q2 == 'all' and q3 == 'french':
                results_sentence = Sentence.objects.filter(content__icontains=q1).order_by('id')
                total_results_sentence = len(results_sentence)
                results = {'results_sentence': results_sentence,
                           'total_results_sentence':total_results_sentence,
                           'chapter_titles':chapter_titles,
                           'text_language':['french','english','chinese'],
                           'q1':q1,
                           'q2':q2,
                           'q3':q3,
                           }
                return results
            elif q2 == 'all' and q3 == 'english':
                results_sentence = Sentence.objects.filter(translation_eng__icontains=q1).order_by('id')
                total_results_sentence = len(results_sentence)
                results = {'results_sentence': results_sentence,
                           'total_results_sentence':total_results_sentence,
                           'chapter_titles':chapter_titles,
                           'text_language':['french','english','chinese'],
                           'q1': q1,
                           'q2': q2,
                           'q3': q3,
                           }
                return results
            elif q3 == 'french':
                results_sentence = Sentence.objects.filter(content__icontains=q1,chapter_title__title_name=q2).order_by('id')
                total_results_sentence = len(results_sentence)
                results = {'results_sentence': results_sentence,
                           'total_results_sentence':total_results_sentence,
                           'chapter_titles':chapter_titles,
                           'text_language':['french','english','chinese'],
                           'q1': q1,
                           'q2': q2,
                           'q3': q3,
                           }
                return results
            elif q3 == 'english':
                results_sentence = Sentence.objects.filter(translation_eng__icontains=q1,chapter_title__title_name=q2).order_by('id')
                total_results_sentence = len(results_sentence)
                results = {'results_sentence': results_sentence,
                           'total_results_sentence':total_results_sentence,
                           'chapter_titles':chapter_titles,
                           'text_language':['french','english','chinese'],
                           'q1': q1,
                           'q2': q2,
                           'q3': q3,
                           }
                return results

        return Sentence.objects.all().order_by('-id')