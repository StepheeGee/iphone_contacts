# contacts/forms.py

from django import forms

class VCFUploadForm(forms.Form):
    vcf_file = forms.FileField()
