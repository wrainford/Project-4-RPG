from django.contrib import admin
from .models import Character, Item, Monster, ThroughModel

# Register your models here.

admin.site.register(Character)
admin.site.register(Monster)
admin.site.register(Item)
admin.site.register(ThroughModel)