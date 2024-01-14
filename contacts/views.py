from django.urls import reverse_lazy, reverse
from contacts.models import Contact
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView,
)
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ContactForm


class ContactsListView(ListView):
    model = Contact
    template_name = "contacts/list.html"
    context_object_name = "contacts"

    def get_queryset(self):
        search = self.request.GET.get("q")
        if search:
            return Contact.objects.filter(
                Q(first__icontains=search)
                | Q(last__icontains=search)
                | Q(phone__icontains=search)
                | Q(email__icontains=search)
            )
        return Contact.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("q")
        return context


class ContactsDetailView(DetailView):
    model = Contact
    template_name = "contacts/detail.html"


class ContactsCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = "contacts/create.html"
    form_class = ContactForm
    success_url = reverse_lazy("contacts")
    success_message = "Created New Contact"


class ContactsUpdateView(SuccessMessageMixin, UpdateView):
    model = Contact
    template_name = "contacts/update.html"
    form_class = ContactForm
    success_message = "Contact Updated!"

    def get_success_url(self):
        return reverse("contacts_update", kwargs={"pk": self.object.id})


class ContactsDeleteView(SuccessMessageMixin, DeleteView):
    model = Contact
    success_message = "Contact Deleted!"
    success_url = reverse_lazy("contacts")
