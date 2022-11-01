from django import forms
from .models import *


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image'].empty_label = "Изображение"
        self.fields['description'].empty_label = "Описание"

    class Meta:
        model = Post
        fields = ['image', 'description']
        widgets = {
            'image': forms.ImageField(),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5, 'class': 'input'}),
        }
