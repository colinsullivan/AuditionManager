from django.contrib import admin

from django.forms import ModelForm
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

from productions.models import *
from auditions.models import *

from django.contrib.admin.sites import AdminSite

admin_site = AdminSite()

# Allow administration of admin users
admin_site.register(User)

# Allow administration of productions
admin_site.register(ProductionType)

class ProductionAdmin(admin.ModelAdmin):
  list_display = ('name', 'default_production')
  
admin_site.register(Production, ProductionAdmin)

# The form which is used for each audition when editing an actor.
class AuditionInlineForm(ModelForm):
  model = Audition
  
  def __init__(self, *args, **kwargs):
    super(AuditionInlineForm, self).__init__(*args, **kwargs)
    
    # set the default to whichever production has default_production set to True
    try:
      defaultProduction = Production.objects.get(default_production = True)
      self.fields['production'].initial = defaultProduction
    except ObjectDoesNotExist, e:
      # There is no default, no need to do anything
      pass

class AuditionInline(admin.StackedInline):
  model = Audition
  extra = 1
  
  def __init__(self, *args, **kwargs):
    # Call parent init
    super(AuditionInline, self).__init__(*args, **kwargs)

    # Use our form subclass
    self.form = AuditionInlineForm
  

class ActorAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'city', 'state', 'age_range', 'thumbnail_img_tag')
  inlines = [
    AuditionInline,
  ]
  
# Allow administration of actors and auditions
admin_site.register(Actor, ActorAdmin)