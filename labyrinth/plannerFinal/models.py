from django.db import models

# Classes, organizations, misc, etc.
class Domains(models.Model):
    domain_name = models.CharField(max_length=100)
    start_date = models.DateField("Beginning Date")
    end_date = models.DateField("Ending Date")
    description = models.CharField(max_length=300)



# Notes, quotes, events, etc.
class Entities(models.Model):
    entity_name = models.CharField(max_length=100)
    start_date_time = models.DateTimeField("Entry Date")
    end_date_time = models.DateTimeField("Due Date")
    text = models.TextField("Notes")


# Check this: https://www.techwithtim.net/tutorials/django/sqlite3-database
# Need to check above in the planner (not plannerFinal) app