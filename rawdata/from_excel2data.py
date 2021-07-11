from rawdata.models import Source,Rawdata,NLP_token_Rawdata
from original_text.models import Sentence,Token,Lemma,Book,Chapter
import xlrd,xlsxwriter
import os
from FLV4_1 import settings
from django.core.exceptions import ObjectDoesNotExist
import spacy




# STEP 1: 先把整理好的法文和英文对应的句子的excel表格，在后台Sentence这个地方，传入系统。这个步骤是人工手动。这个步骤的模板excel表格就是Sentence。
# STEP 2: 从Sentence这个数据表里，通过使用filter方式找到刚放入的句子们，然后使用NLP清点每一个句子的token.
sentence_datas = Sentence.objects.filter(pk__range=[3269,3841])
sentence_total = len(sentence_datas)
print(sentence_total)


nlp = spacy.load('fr_dep_news_trf')
y = 1
for data in sentence_datas:
    lowered_text = data.content.lower()
    data.content_lower_case = lowered_text
    doc = nlp(lowered_text)
    total_token = []
    for token in doc:
        total_token.append(token)
    len_total_token = len(total_token)
    data.token_total_french = len_total_token
    data.note = 'HarryPotter Book 1'
    data.save()
    print(f'---{len_total_token} TOKENS----{y} SENTENCE OUT OF {sentence_total} ----------------')
    y = y+1


# STEP 3: 从Sentence这个数据表里，通过使用filter方式找到刚放入的句子们，然后使用NLP，整理出每一句话里的token。
# STEP 3.1: 先清空NLP_token_Rawdata，所以才可以把从Sentence里分析出的token存入NLP_token_Rawdata的表里。记得note='HarryPotter Book 1 tokens'
datas = NLP_token_Rawdata.objects.all()
total_datas =len(datas)
print(total_datas)

sentence_datas = Sentence.objects.filter(pk__range=[3269,3841])
sentence_total = len(sentence_datas)
print(sentence_total)

nlp = spacy.load('fr_dep_news_trf')

y = 1
for data in sentence_datas:
    lowered_text = data.content_lower_case
    doc = nlp(lowered_text)
    len_total_token = data.token_total_french
    i = 1
    for token in doc:
        new_token = NLP_token_Rawdata.objects.create(sentence_id=data.id)
        new_token.chapter_id = data.chapter_id.id
        new_token.book_id = data.book_id.id
        new_token.sentence_number = data.number
        new_token.token_language = 'french'
        new_token.sentence = data.content
        new_token.nlp_text = token.text
        new_token.nlp_pos = token.pos_
        new_token.nlp_tag = token.tag_
        new_token.nlp_dep = token.dep_
        new_token.nlp_lemma = token.lemma_
        new_token.token_nunmber = i
        new_token.note = 'HarryPotter Book 1 tokens'
        new_token.save()
        print(f'-------{i} TOKEN OUT OF {len_total_token} ----------------')
        i = i + 1
    print(f'-------{y} SENTENCE OUT OF {sentence_total} ----------------')
    y = y+1




# STEP 3.2: 从token的数据里，读出lemma。
# STEP 3.3: 把新读出的lemma与已经存在的lemma做比较，把新的lemma存入Lemma表里

datas_tokens = NLP_token_Rawdata.objects.filter(note = 'HarryPotter Book 1 tokens')
total_tokens=len(datas_tokens)

i = 1
lemma_list = []
for data in datas_tokens:
    lemma = data.nlp_lemma
    lemma_list.append(lemma)
    print(f'-------{i} TOKEN OUT OF {total_tokens} ----------------')
    i = i + 1

lemma_list_duplicated_removed = list(dict.fromkeys(lemma_list))
total_lemmas = len(lemma_list_duplicated_removed)
print(total_lemmas)

i = 1
for lemma in lemma_list_duplicated_removed:
    try:
        exist = Lemma.objects.get(text=lemma)
        print(f'-------ALREADY---------')
        print(f'-------{i} TOKEN OUT OF {total_lemmas} ----------------')
        i = i + 1
    except Lemma.DoesNotExist:
        new_lemma = Lemma.objects.create(text=lemma)
        new_lemma.lemma_language = 'french'
        new_lemma.save()
        print(f'-------{i} TOKEN OUT OF {total_lemmas} ----------------')
        i = i + 1



# STEP 3.4: 把Rawdata里note='tokens'的数据，写入Token这张表里。

datas_tokens = NLP_token_Rawdata.objects.filter(note='HarryPotter Book 1 tokens')
total_tokens=len(datas_tokens)
print(total_tokens)

i = 1
for data in datas_tokens:
    book = Book.objects.get(id=data.book_id)
    print(book.pk)
    chapter = Chapter.objects.get(id=data.chapter_id)
    print(chapter.pk)
    sentence = Sentence.objects.get(id=data.sentence_id)
    print(sentence.pk)
    lemma = Lemma.objects.get(text=data.nlp_lemma)
    print(lemma.pk)
    print(f'-----LEMMA: {lemma}------')
    token = Token.objects.create(book_id=book,chapter_id=chapter,sentence_id=sentence,token_lemma=lemma)
    token.sentence_number = data.sentence_number
    token.token_language = data.token_language
    token.pos = data.nlp_pos
    token.tag = data.nlp_tag
    token.dep = data.nlp_dep
    token.token_nunmber = data.token_nunmber
    token.note = 'HarryPotter Book 1'
    token.save()
    print(f'-------{i} TOKEN OUT OF {total_tokens} ----------------')
    i = i + 1


# STEP 4: 手动从admin里到处Lemma和Token这两张表。然后手动在FLV4_1的admin里去传入。
