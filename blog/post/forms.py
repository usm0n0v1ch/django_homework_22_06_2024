from django import forms

from post.models import Post, Comment, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','content']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']