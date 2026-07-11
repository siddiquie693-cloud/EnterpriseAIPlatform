from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Create default user group."

    def handle(self, *args, **kwargs):
        groups = [
            "Admin",
            "Manager",
            "Employee",
        ]

        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)

            if created:
                self.stdout.write(self.style.SUCCESS(f"{group_name} group created."))
            else:
                self.stdout.write(self.style.WARNING(f"{group_name} group already exists."))    