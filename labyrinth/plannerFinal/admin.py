from django.contrib import admin
from .models import Domain, TimedEntity, UntimedEntity

admin.site.register(Domain)
admin.site.register(TimedEntity)
admin.site.register(UntimedEntity)