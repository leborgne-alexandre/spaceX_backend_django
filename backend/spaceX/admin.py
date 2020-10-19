from django.contrib import admin
from .models import SpaceX # add this

class SpaceXAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description') # add this

# Register your models here.
admin.site.register(SpaceX, SpaceXAdmin) # add this