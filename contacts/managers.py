from django.db import models
import csv
from io import StringIO


class ContactManager(models.Manager):
    def export_to_csv(self):
        queryset = self.all()
        field_names = [field.name for field in self.model._meta.fields]
        csv_file = StringIO()
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(field_names)
        for record in queryset:
            csv_writer.writerow([getattr(record, field) for field in field_names])
        csv_file.seek(0)

        return csv_file
