from django.shortcuts import render
from django.http import HttpResponse
from .models import Domain, UntimedEntity, TimedEntity


def index(request, id):
    # return render(request, "plannerFinal/base.html", {})
    ls = Domain.objects.get(id=id)
    timedEntities = ls.timedentity_set.get(id=1)
    untimedEntities = ls.untimedentity_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><p>%s</p><br><p>%s</p>" %(ls.domain_name, timedEntities.text, untimedEntities.text)) 


def labyrinth(request):
    pass