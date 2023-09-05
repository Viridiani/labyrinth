from django import template

register = template.Library()


# Keep in mind it has to be from obj.Objects.all()
@register.filter(name="from_domain")
def in_domain(obj, domain):
    return obj.filter(domains=domain)

# Need to have a filter which gets an id?