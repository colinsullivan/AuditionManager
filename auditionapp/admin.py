from django.contrib import admin

from django.forms import ModelForm
from django.contrib.auth.models import User

from productions.models import *
from auditions.models import *

from django.contrib.admin.sites import AdminSite

admin_site = AdminSite()

# Allow administration of admin users
admin_site.register(User)

# Allow administration of productions
admin_site.register(ProductionType)
admin_site.register(Production)

# Show addresses inline for actors
class AddressInline(admin.StackedInline):
  model = Address
  max_num = 1
  exclude = ('latitude', 'longitude')

class ActorAdmin(admin.ModelAdmin):
  inlines = [
    AddressInline,
  ]
  
# Allow administration of actors and auditions
admin_site.register(Actor, ActorAdmin)
admin_site.register(Audition)
