from django.db import models

# Classes, organizations, misc, etc.
class Domains(models.Model):
    domain_name = models.CharField(max_length=100)
    start_date = models.DateField("Beginning Date")
    end_date = models.DateField("Ending Date")



# Notes, quotes, events, etc.
class Entities(models.Model):
    entity_name = models.CharField(max_length=100)
    start_date_time = models.DateTimeField("Entry Date")
    end_date_time = models.DateTimeField("Due Date")


# need to add admin login as well?? probably not
# Check this: https://www.techwithtim.net/tutorials/django/sqlite3-database
# Because to some extent, Events/Organizations and ToDoList/Items should be the same
# Need to check that in the planner (not plannerFinal) app
# This will actually need to be sketched out for database planning