from django.db import models
from original_text.models import Token, Sentence
from django.contrib.auth.models import User

# Create your models here.

class MyWord(models.Model):
    token_id = models.ForeignKey(Token, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    mynote4review = models.CharField(max_length=500, default='None. To be updated.')
    related_token_id = models.ForeignKey(Token, on_delete=models.CASCADE,related_name='related_token')
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.mynote4review
