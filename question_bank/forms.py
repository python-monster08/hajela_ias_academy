from django import forms
from tinymce.widgets import TinyMCE
from .models import InputSuggestion

class InputSuggestionForm(forms.ModelForm):
    details = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = InputSuggestion
        fields = [
            'language', 'script', 'evergreen_index', 'brief_description', 'details',
            'exam_name', 'subject_name', 'area_name', 'part_name', 'chapter_name',
            'topic_name', 'question_video', 'question_link', 'other_text'
        ]
        
class UploadFileForm(forms.Form):
    file = forms.FileField()


