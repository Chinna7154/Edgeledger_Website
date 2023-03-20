from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    message = forms.CharField(widget=forms.Textarea)
