from django.shortcuts import render, redirect
from .models import Registration
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


# Create your views here.
def registration(request):
    name = request.GET.get('name')
    if name is not None:
        new_user = Registration(Name=name)
        new_user.save()
        return redirect(f'http://{IPAddr}:8000/{name}')
    return render(request, 'chat/Name.html')


def lobby(request, name):
    people = Registration.objects.all()
    name = {
        'name': name,
        'people': people,
        'IP_add': f"http://{IPAddr}:8000",
    }
    return render(request, 'chat/lobby.html', name)


def logout(request, name):
    user = Registration.objects.get(Name=name)
    user.delete()
    return redirect('/')
