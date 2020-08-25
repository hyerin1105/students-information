from django import forms
from .models import Information

class InfForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class' : 'inf_title',
            'placeholder' : '제목',
        })
        self.fields['content'].widget.attrs.update({
            'class' : 'inf_content_form',
        })