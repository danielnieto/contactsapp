from django import forms


class EmailHTMXWidget(forms.EmailInput):
    template_name = "contacts/widgets/email_htmx_widget.html"
