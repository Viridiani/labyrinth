from django.db import models


class Notes(models.Model):
    pass


class Events(models.Model):
    pass


class Organizations(models.Model):
    pass


class Quotes(models.Model):
    pass


# Same with these two
class ToDoList(models.Model):
    pass


class Items(models.Model):
    pass


# need to add admin login as well :/
# Check this: https://www.techwithtim.net/tutorials/django/sqlite3-database
# Because to some extent, Events/Organizations and ToDoList/Items should be the same
# Need to check that in the planner (not plannerFinal) app