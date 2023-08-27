from django.db import models

# Classes, organizations, misc, etc.
class Domains(models.Model):
    pass


# Notes, quotes, events, etc.
class Entities(models.Model):
    pass


# need to add admin login as well?? probably not
# Check this: https://www.techwithtim.net/tutorials/django/sqlite3-database
# Because to some extent, Events/Organizations and ToDoList/Items should be the same
# Need to check that in the planner (not plannerFinal) app
# This will actually need to be sketched out for database planning