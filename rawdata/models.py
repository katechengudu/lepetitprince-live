from django.db import models

# Create your models here.

class Source(models.Model):
    title = models.CharField(max_length=100, blank=True)
    file = models.FileField(null=True,blank=True,upload_to='rawdata/source/')
    note = models.CharField(max_length=100,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Rawdata(models.Model):
    source_title = models.ForeignKey(Source,on_delete=models.CASCADE)
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




