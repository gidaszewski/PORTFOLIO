from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Destinatario')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')