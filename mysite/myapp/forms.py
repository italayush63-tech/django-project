from django import forms
from .models import Message, Post

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email' , 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']        