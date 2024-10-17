import pandas as pd
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from .forms import UploadFileForm

def handle_uploaded_file(f):
   
    if f.name.endswith('.csv'):
        df = pd.read_csv(f)
    elif f.name.endswith('.xlsx'):
        df = pd.read_excel(f)
    else:
        return None

    df = df[['Cust State', 'Cust Pin', 'DPD']]
    
   
    summary_html = df.to_html(index=False, justify='center', header=True)
    
    return summary_html


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            summary_html = handle_uploaded_file(uploaded_file)
            
            if summary_html:
               
                send_mail(
                    subject="python Assignment VICKY KUMAR",
                    message="this is my assignement by Medius",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['tech@themedius.ai'],
                    html_message=summary_html,  # Send the formatted table as HTML
                    fail_silently=False,
                )
                return HttpResponseRedirect('/success/')
            else:
                return HttpResponse('Invalid file format. Please upload an Excel/CSV file.')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})


def success(request):
    return render(request,"success.html")    
