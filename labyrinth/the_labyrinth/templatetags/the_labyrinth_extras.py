from django import template

register = template.Library()


# Keep in mind it has to be from obj.Objects.all()
@register.filter(name="from_domain")
def in_domain(obj, domain):
    return obj.filter(domains=domain)

# Filter which should sort from obj.Objects.all() or from the filtered by domains and give back by due date
def sort_date(obj):
    return obj.order_by('end_date_time')