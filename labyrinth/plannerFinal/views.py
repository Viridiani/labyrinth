from django.shortcuts import render
from .models import Domain, UntimedEntity, TimedEntity


# Testing page for domains and their entities
def base(request, domain_name):
    name = str(domain_name).title()
    domain = Domain.objects.get(domain_name=name)
    pid = domain.pk
    d = [domain.domain_name, domain.start_date, domain.end_date, domain.description]
    untimedEntity = UntimedEntity.objects.filter(domains=pid).all()
    u = []
    for i in untimedEntity:
        u.append([i.domains, i.entity_name, i.category, i.text])
    timedEntity = TimedEntity.objects.filter(domains=pid).all()
    t = []
    for i in timedEntity:
        t.append([i.domains, i.entity_name, i.category, i.start_date_time, i.end_date_time, i.text, i.complete])

    baseData = {"domain_name":domain, "domain_content":d, "untimedEntity":untimedEntity, "untimedEntity_content": u, "timedEntity":timedEntity, "timedEntity_content": t}
    return render(request, "plannerFinal/base.html", baseData) 


# Main page
def labyrinth(request):
    return render(request, "plannerFinal/labyrinth.html", {})