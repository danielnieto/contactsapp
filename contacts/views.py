from django.shortcuts import render, redirect
from django.urls import reverse
from contacts.models import Contact
from django.db.models import Q
from django.views import View
from django.contrib import messages


def index(request):
    return redirect("contacts")


def contacts(request):
    search = request.GET.get("q")

    if search:
        contacts = Contact.objects.filter(
            Q(first__icontains=search)
            | Q(last__icontains=search)
            | Q(phone__icontains=search)
            | Q(email__icontains=search)
        )
    else:
        contacts = Contact.objects.all()
    return render(
        request, "contacts/index.html", {"contacts": contacts, "search": search}
    )


class ContactsNewView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contacts/new.html", {"contact": Contact()})

    def post(self, request, *args, **kwargs):
        Contact.objects.create(
            first=request.POST.get("first_name"),
            last=request.POST.get("last_name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
        )
        messages.success(request, "Created New Contact!")
        return redirect(reverse("contacts_new"))
