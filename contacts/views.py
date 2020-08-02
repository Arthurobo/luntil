from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully, we will get back to you soon.")
            # messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('contact')

    else:
        form = ContactForm()
    return render(request, 'contacts/contact.html', {'form': form})


"""
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            email_send = EmailMessage("New contact form submission",
                                      "Subject: " + subject + '\n'
                                      'Name: ' + name + '\n' 
                                      "Email: " + email + '\n'
                                      'Message: ' + message,
                                      "Anonima" + ' ', ['arthuron57@gmail.com', 'arthuron2000@gmail.com', ],
                                      headers={'Reply-To': email})
            email_send.send()

            form.save()
            messages.success(request, "Your message was sent successfully, we will get back to you soon.")
            # messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('contact')

    else:
        form = ContactForm()
    return render(request, 'contact/contact2.html', {'form': form})
"""
