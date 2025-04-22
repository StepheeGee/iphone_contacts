# contacts/forms.py

from django import forms

class VCFUploadForm(forms.Form):
    vcf_file = forms.FileField()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
