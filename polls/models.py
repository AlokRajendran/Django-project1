from django.db import models
from django.db.models.fields import CharField
import datetime
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text= models.CharField(max_length=100)
    pub_date= models.DateTimeField('date published')
    active= models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.question_text

       
    @admin.display(boolean=True, ordering= "pub_date", description="is publised recently")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        

class Choice(models.Model):
    question= models.ForeignKey(Question,on_delete= models.CASCADE)
    choice_text= models.CharField(max_length=100)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text