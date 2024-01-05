from django.urls import path
from contacts import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contacts", views.contacts, name="contacts"),
    path("contacts/new", views.ContactsNewView.as_view(), name="contacts_new"),
    path("contacts/<int:pk>", views.contacts_detail, name="contacts_detail"),
]
