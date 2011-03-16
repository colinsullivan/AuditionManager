from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, BaseModelFormSet
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.forms import USStateSelect, USZipCodeField


from auditions.models import Actor, Address

class ActorSignupForm(ModelForm):
  """A form that allows an actor to signup"""
#  age_range = models.IntegerField(max_length=1, choices=AGE_CHOICES)
#  height = models.CharField(max_length=128)
#  size = models.CharField(max_length=128)
#  union = models.CharField(max_length=128)
#  special = models.TextField(blank=None)
#  reference = models.TextField(blank=None)
  
  
  class Meta:
    model = Actor

  def __init__(self, *args, **kwargs):
    super(ActorSignupForm, self).__init__(*args, **kwargs)
    
    self.fields['size'].label = _('Suit/Dress size')
    self.fields['union'].label = _('Union or Non-Union? (SAG, AFTRA, etc.)')
    self.fields['special'].label = _('Special Abilities')
    self.fields['reference'].label = _('How did you hear about us? (Include talent agency if applicable)')
    


class AddressForm(ModelForm):
  line1 = forms.CharField(max_length = 128, label=_('Address line 1'))
  line2 = forms.CharField(max_length = 128, label=_('Address line 2'), required=False)
  city = forms.CharField(max_length = 128, label=_('City'))
  state = USStateSelect()
  zipcode = USZipCodeField()
  
  class Meta:
    exclude = ('latitude', 'longitude')
    
    
ActorSignupAddressFormset = inlineformset_factory(Actor, Address, max_num=1, form=AddressForm, can_delete=False)
