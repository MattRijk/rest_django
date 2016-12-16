from django import forms
# from pagedown.widgets import PagedownWidget
from posts.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.Textarea()
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]