from django.shortcuts import render
from .models import Domain, UntimedEntity, TimedEntity

# my_dict = {} # can be passed into render()
data = {}

# Testing page for domains and their entities
def base(request, domain_name):
    name = str(domain_name).title()
    domain = Domain.objects.get(domain_name=name)
    pid = domain.pk
    untimedEntity = UntimedEntity.objects.filter(domains=pid).all()
    timedEntity = TimedEntity.objects.filter(domains=pid).all()
    return render(request, "plannerFinal/base.html", {"domain_name":domain, "untimedEntity":untimedEntity, "timedEntity":timedEntity}) 


# Main page
def labyrinth(request):
    return render(request, "plannerFinal/labyrinth.html", {})