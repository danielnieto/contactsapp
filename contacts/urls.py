from django.urls import path
from contacts import views
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="contacts"), name="index"),
    path("contacts", views.ContactsListView.as_view(), name="contacts"),
    path("contacts/create", views.ContactsCreateView.as_view(), name="contacts_create"),
    path("contacts/<int:pk>", views.ContactsCRUDView.as_view(), name="contacts_crud"),
    path(
        "contacts/<int:pk>/update",
        views.ContactsUpdateView.as_view(),
        name="contacts_update",
    ),
]
