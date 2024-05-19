from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
# Create your views here.
bookList = ['Ai tools','Django for example']
def books(request):
    return render(request,"books.html",{'books':bookList})

def add(request):
    return render(request,"add.html")


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'your_app/add_client.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'your_app/client_list.html', {'clients': clients})
