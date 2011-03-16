from django.template import RequestContext
from django.shortcuts import render_to_response

from auditions.forms import ActorSignupForm, ActorSignupAddressFormset



# This view allows actors to sign up.
def actorsignup(request):
  signupForm = ActorSignupForm()
  addressFormset = ActorSignupAddressFormset()
  
  return render_to_response('actor_signup.html', {
    'signupForm': signupForm, 
    'addressFormset': addressFormset.forms[0], 
  }, context_instance = RequestContext(request))
