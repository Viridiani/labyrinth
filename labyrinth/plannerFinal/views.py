from django.shortcuts import render
from .models import Domain, UntimedEntity, TimedEntity


# Testing page for domains and their entities
def base(request, id):
    # my_dict = {} # can be passed into render()
    ls = Domain.objects.get(id=id)
    # timedEntities = ls.timedentity_set.get(id=1)
    # untimedEntities = ls.untimedentity_set.get(id=1)
    return render(request, "plannerFinal/base.html", {"domain_name": ls.domain_name}) 


# Main page
def labyrinth(request):
    return render(request, "plannerFinal/labyrinth.html", {"domain_name": "test"})