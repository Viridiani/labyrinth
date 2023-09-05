from django.db import models

# Classes, organizations, misc, etc.
class Domain(models.Model):
    domain_name = models.CharField(max_length=100)
    start_date = models.DateField("Beginning Date")
    end_date = models.DateField("Ending Date")
    description = models.CharField(max_length=300)


    def __str__(self):
        return self.domain_name


# Notes, quotes, events, etc.
class TimedEntity(models.Model):
    domains = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="timedEntity")
    # Use a foreign key (domain object when creating an item)
    # When deleting a Domain, remove all entities beneath it
    entity_name = models.CharField(max_length=100)
    category = models.CharField(max_length = 100)
    start_date_time = models.DateTimeField("Entry Date")
    end_date_time = models.DateTimeField("Due Date")
    text = models.TextField("Description")
    complete = models.BooleanField()


    def __str__(self):
        return self.entity_name


class UntimedEntity(models.Model):
    domains = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="untimedEntity")
    entity_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    text = models.TextField("Notes")


    def __str__(self):
        return self.entity_name


"""
Getting into the command line
python manage.py shell
commands for sql database stuff:
from the_labyrinth.models import Domain, TimedEntity, Untimed Entity
d = Domain(domain_name="...", start_date="...", end_date="...", description="...")
d.save()
Domain.objects.all()
"""