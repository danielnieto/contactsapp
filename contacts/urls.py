from django.urls import path
from contacts import views
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="contacts"), name="index"),
    path("contacts", views.ContactsListView.as_view(), name="contacts"),
    path("contacts/create", views.ContactsCreateView.as_view(), name="contacts_create"),
    path(
        "contacts/<int:pk>", views.ContactsDetailView.as_view(), name="contacts_detail"
    ),
    path(
        "contacts/<int:pk>/update",
        views.ContactsUpdateView.as_view(),
        name="contacts_update",
    ),
    path(
        "contacts/<int:pk>/delete",
        views.ContactsDeleteView.as_view(),
        name="contacts_delete",
    ),
]
