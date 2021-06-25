from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300,null=True, blank=True)
    author = models.CharField(max_length=300,null=True, blank=True)
    translation_eng = models.TextField(null=True,blank=True)
    translation_chi = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=500,default='none')
    priority = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

class Chapter(models.Model):
    book_title = models.ForeignKey(Book,on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)
    title_name = models.CharField(max_length=300,null=True, blank=True)
    title_number = models.IntegerField(null=True, blank=True)
    translation_eng = models.TextField(null=True,blank=True)
    translation_chi = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=500,default='none')
    priority = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    def __str__(self):
        return self.note


class Sentence(models.Model):
    chapter_title = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    content_lower_case = models.TextField(null=True, blank=True)
    translation_eng = models.TextField(null=True,blank=True)
    translation_chi = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=500,default='none')
    priority = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    def __str__(self):
        return self.note
