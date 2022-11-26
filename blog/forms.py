from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# new
class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'category',
            'content',
            'excerpt',
            'featured_image',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
