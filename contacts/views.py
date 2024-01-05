from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contacts.models import Contact
from django.db.models import Q
from django.views import View
from django.contrib import messages

from .forms import ContactForm


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


def contacts_detail(request, pk: int):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/detail.html", {"contact": contact})


class ContactsNewView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contacts/new.html", {"form": ContactForm()})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if not form.is_valid():
            return render(request, "contacts/new.html", {"form": form})

        form.save()
        messages.success(request, "Created New Contact!")
        return redirect(reverse("contacts"))


class ContactsEditView(View):
    def get(self, request, pk: int):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(instance=contact)
        return render(request, "contacts/edit.html", {"form": form, "contact": contact})

    def post(self, request, pk: int):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST, instance=contact)

        if not form.is_valid():
            return render(
                request, "contacts/edit.html", {"form": form, "contact": contact}
            )

        form.save()
        messages.success(request, "Contact Updated!")
        return redirect(reverse("contacts_edit", kwargs={"pk": contact.id}))


def contacts_delete(request, pk: int):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    messages.success(request, "Contact Deleted!")
    return redirect(reverse("contacts"))
