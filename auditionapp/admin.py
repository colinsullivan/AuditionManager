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

class ActorAdmin(admin.ModelAdmin):
  pass
  
# Allow administration of actors and auditions
admin_site.register(Actor, ActorAdmin)
admin_site.register(Audition)
