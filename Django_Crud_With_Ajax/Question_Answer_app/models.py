from django.db import models

# Create your models here.
class QuestionsAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()


    def __str__(self):
        return self.question