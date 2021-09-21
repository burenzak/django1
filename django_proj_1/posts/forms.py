from .models import Post
from django.forms import ModelForm, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': Textarea()
        }