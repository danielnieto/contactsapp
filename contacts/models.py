from django.db import models


class Contact(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)  # Assuming phone numbers as strings
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first} {self.last}"
