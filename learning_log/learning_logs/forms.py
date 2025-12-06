from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields = ['question','text']
        labels = {'question': '','text': ''}
        widgets = {'question': forms.Textarea(attrs={'cols': 80, 'rows': 5}), 'text': forms.Textarea(attrs={'cols': 80})}
