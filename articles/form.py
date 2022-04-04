from django import forms

class AddArticle(forms.Form):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'form_title_article'}))
    text = forms.CharField(label='text', max_length=500, widget=forms.TextInput(attrs={'class': 'form_text_article'}))

class AddLike(forms.Form):
    like_button = forms.BooleanField(label='like', required=False)
