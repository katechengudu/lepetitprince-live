from django.db import models

# Create your models here.

class Source(models.Model):
    title = models.CharField(max_length=100, blank=True)
    file = models.FileField(null=True,blank=True,upload_to='raw_data/source/')
    note = models.CharField(max_length=100,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Rawdata(models.Model):
    source_title = models.ForeignKey(Source,on_delete=models.CASCADE,null=True, blank=True)
    book_id = models.IntegerField(null=True, blank=True)
    chapter_id = models.IntegerField(null=True, blank=True)
    sentence_id = models.IntegerField(null=True, blank=True)
    sentence_number = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    content_lower_case = models.TextField(null=True, blank=True)
    translation_eng = models.TextField(null=True,blank=True)
    translation_chi = models.TextField(null=True, blank=True)
    token_total_french = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=500,default='none')
    priority = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    def __str__(self):
        return self.note


class NLP_token_Rawdata(models.Model):
    source_sentence = models.ForeignKey(Rawdata,on_delete=models.CASCADE,null=True, blank=True)
    book_id = models.IntegerField(null=True, blank=True)
    chapter_id = models.IntegerField(null=True, blank=True)
    sentence_id = models.IntegerField(null=True, blank=True)
    sentence_number = models.IntegerField(null=True, blank=True)
    sentence = models.CharField(max_length=2000,null=True,blank=True)
    token_language = models.CharField(max_length=50, default='french')
    nlp_text = models.CharField(max_length=800,null=True,blank=True)
    nlp_lemma = models.CharField(max_length=800,null=True,blank=True)
    nlp_pos = models.CharField(max_length=800,null=True,blank=True)
    nlp_tag = models.CharField(max_length=800,null=True,blank=True)
    nlp_dep = models.CharField(max_length=800, null=True, blank=True)
    note = models.CharField(max_length=800,null=True,blank=True)
    token_nunmber = models.IntegerField(null=True, blank=True)
    vocab_frequency_score = models.IntegerField(null=True, blank=True)
    notes_vocab_frequency_score = models.BooleanField(default=False)

    def __str__(self):
        return self.nlp_text



