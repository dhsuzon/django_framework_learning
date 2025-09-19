from django import forms
from post.models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model =  PostModel
        fields = "__all__"

        