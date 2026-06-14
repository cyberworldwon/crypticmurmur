from django import forms

class EntryForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your name')
    message = forms.CharField(
        max_length=300,
        label='Message',
        widget=forms.Textarea
    )