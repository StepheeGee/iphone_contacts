from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import VCFUploadForm, ContactForm  # ⬅️ add ContactForm
from .utils import parse_vcf_to_xls
import tempfile

def upload_vcf(request):
    if request.method == 'POST':
        form = VCFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            vcf_file = request.FILES['vcf_file']
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_xls:
                    parse_vcf_to_xls(vcf_file, temp_xls.name)
                    temp_xls.seek(0)
                    response = HttpResponse(
                        temp_xls.read(),
                        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    )
                    response['Content-Disposition'] = 'attachment; filename="contacts.xlsx"'
                    messages.success(request, "✅ Contacts converted and ready for download!")
                    return response
            except Exception as e:
                print("VCF Parse Error:", e)
                messages.error(request, "⚠️ Failed to convert the VCF file. Make sure it's valid.")
                return redirect('upload_vcf')
    else:
        form = VCFUploadForm()

    return render(request, 'contacts/upload.html', {'form': form})


# ✅ Privacy Policy View
def privacy_policy(request):
    return render(request, 'contacts/privacy.html')


# ✅ Contact Form View
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # (Optional) Save or send email here
            messages.success(request, "Thanks for reaching out! We'll get back to you soon.")
            return redirect('contact')  # prevents re-submission on refresh
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contact.html', {'form': form})
