from django import forms

class UrlForms(forms.Form):
    url = forms.URLField(label="enter the URL", widget=forms.URLInput(attrs={'placeholder': "https://chatgpt.com/",}))
