from django.shortcuts import render, redirect
from contacts.models import Contact
from django.db.models import  Q

def index(request):
    return redirect("contacts")

def contacts(request):
    search = request.GET.get('q')

    if search:
        contacts = Contact.objects.filter(
                Q(first__icontains=search) |
                Q(last__icontains=search) |
                Q(phone__icontains=search) |
                Q(email__icontains=search)
            )
    else:
        contacts = Contact.objects.all()
    return render(request, "contacts/index.html", {'contacts': contacts, 'search': search})


def contacts_new_get(request):
    return render(request, "contacts/new.html", {'contact': Contact()})
    
