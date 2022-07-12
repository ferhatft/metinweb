from django.shortcuts import render,redirect

from .models import Contact,Teklif
from django.core.mail import send_mail
from .forms import ContactForm,TeklifForm



def contacview(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name        = form.cleaned_data['name']
            email       = form.cleaned_data['email']
            message     = form.cleaned_data['message']

# dev
            send_mail (
                name , # subject
                'Gönderen = ' + email + '\n' + message , #message
                'oref.tasarim@gmail.com', #from email
                ['tugrul.tf51@gmail.com',], # To email    
            )
# live 
            
            # send_mail (
            #     name , # subject
            #     'Gönderen = ' + email + '\n' + message , #message
            #     'ozdagenis@gmail.com', #from email
            #     ['ozdagenis@gmail.com',], # To email    
            # )

            form.save()
            return redirect('anasayfa')
    else:
        form = ContactForm()



    context = {
        'form': form,
    }
    return render(request, "contact.html", context)





def teklifview(request):

    if request.method == 'POST':
        form = TeklifForm(request.POST)
        if form.is_valid():
#             name        = form.cleaned_data['name']
#             email       = form.cleaned_data['email']
#             message     = form.cleaned_data['message']

# # dev
#             send_mail (
#                 name , # subject
#                 'Gönderen = ' + email + '\n' + message , #message
#                 'oref.tasarim@gmail.com', #from email
#                 ['tugrul.tf51@gmail.com',], # To email    
#             )
# # live 
            
#             # send_mail (
#             #     name , # subject
#             #     'Gönderen = ' + email + '\n' + message , #message
#             #     'ozdagenis@gmail.com', #from email
#             #     ['ozdagenis@gmail.com',], # To email    
#             # )

            form.save()
            return redirect('anasayfa')
    else:
        form = TeklifForm()



    context = {
        'form': form,
    }
    
    return render(request, "teklif.html", context)

