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
    return render(request, "the_labyrinth/base.html", baseData) 


# Main page
domains = Domain.objects.all()
untimedEntities = UntimedEntity.objects.all().order_by('category')
timedEntities = TimedEntity.objects.all().order_by('category', 'end_date_time')
def labyrinth(request):
    return render(request, "the_labyrinth/labyrinth.html", {"d": domains, "u": untimedEntities, "t": timedEntities})