from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, BaseModelFormSet
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.forms import USStateSelect, USZipCodeField, USPhoneNumberField


from auditions.models import Actor

class ActorSignupForm(ModelForm):
  """A form that allows an actor to signup"""
  line1 = forms.CharField(max_length = 128, label=_('Address line 1'), 
    widget=forms.TextInput(attrs={'size': '40'})
  )
  line2 = forms.CharField(max_length = 128, label=_('Address line 2'), 
    required=False,
    widget=forms.TextInput(attrs={'size': '40'})
  )
  city = forms.CharField(max_length = 128, label=_('City'))
  state = USStateSelect()
  zipcode = USZipCodeField()
  phone = USPhoneNumberField(label=_('Phone (xxx-xxx-xxxx)'))

  
  
  class Meta:
    model = Actor

  def __init__(self, *args, **kwargs):
    super(ActorSignupForm, self).__init__(*args, **kwargs)
    
    self.fields['size'].label = _('Suit/Dress size')
    self.fields['union'].label = _('Union or Non-Union? (SAG, AFTRA, etc.)')
    self.fields['special'].label = _('Special Abilities')
    self.fields['reference'].label = _('How did you hear about us? (Include talent agency if applicable)')
