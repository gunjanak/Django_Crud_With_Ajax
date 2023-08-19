from django import forms
from .models import QuestionsAnswer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionsAnswer
        fields = ['question','answer']

        