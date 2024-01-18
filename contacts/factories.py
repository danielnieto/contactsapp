from .models import Contact
from factory.django import DjangoModelFactory
import factory


class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    first = factory.Faker("first_name")
    last = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
