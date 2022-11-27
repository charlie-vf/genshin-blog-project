from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Comment, Post, Category
from django import forms

# List for categories dropdown
categories = Category.objects.all().values_list('name', 'name')
categories_list = []
for item in categories:
    categories_list.append(item)


class CommentForm(forms.ModelForm):
    """ Form for commenting on posts """
    class Meta:
        model = Comment
        fields = ('body',)


class CreateForm(forms.ModelForm):
    """ Form for creating new blog post """
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
            'category': forms.Select(
                choices=categories_list, attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
