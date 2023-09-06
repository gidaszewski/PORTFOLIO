from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponseRedirect, HttpResponseServerError

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def contact(request):
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        remitente = request.POST['remitente']
        destinatario = ['gidaszewskifranco@gmail.com']
        try:
            print(f"Asunto: {asunto}")
            print(f"Mensaje: {mensaje}")
            print(f"Remitente: {remitente}")
            send_mail(asunto, mensaje, remitente, destinatario)
            return HttpResponseRedirect('email-success')
        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")
            return HttpResponseServerError('Error al enviar el correo electrónico.')
    else:
        return render(request, 'Home/contact.html')

def resume(request):
    return render(request, 'Home/resume.html')

def projects(request):
    return render(request, 'Home/projects.html')

def mail_success(request):
    return render(request, 'Home/mail-success.html')