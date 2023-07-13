from django.forms import ModelForm, CharField, TextInput
from .models import Quote,MAX_LENGTH,Tag

class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=MAX_LENGTH, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=MAX_LENGTH, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote','author']
        exclude = ['tags']

class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=MAX_LENGTH, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']