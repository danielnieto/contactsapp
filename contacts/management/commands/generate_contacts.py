from django.core.management.base import BaseCommand
from contacts.factories import ContactFactory


class Command(BaseCommand):
    help = "Generate fake contacts"

    def add_arguments(self, parser):
        parser.add_argument("num", nargs="?", type=int)

    def handle(self, *args, **options):
        num = options["num"]
        ContactFactory.create_batch(num)
        self.stdout.write(self.style.SUCCESS("Created %s contact(s)" % num))
