from django.contrib import admin
from .models import QuestionsAnswer

# Register your models here.
@admin.register(QuestionsAnswer)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question','answer')
