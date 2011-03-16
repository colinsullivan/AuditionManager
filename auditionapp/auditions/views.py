from django.template import RequestContext
from django.shortcuts import render_to_response

from auditions.forms import ActorSignupForm



# This view allows actors to sign up.
def actorsignup(request):
  
  if request.method == 'POST':
    signupForm = ActorSignupForm(request.POST)
    
    if signupForm.is_valid():
      # Create actor
      actor = signupForm.save()
      
      # Forward to success view
      return actorsignupsuccess(request)
      
      
    else:
      # Error message
      message = 'Errors occurred.  Please see below:'
    
  else:
    signupForm = ActorSignupForm()
    message = 'Please enter your audition information:'
  
  return render_to_response('actor_signup.html', {
    'message': message, 
    'signupForm': signupForm, 
  }, context_instance = RequestContext(request))

# This is the view that is used when the actor signup was a success
def actorsignupsuccess(request):
  
  return render_to_response('actor_signup_success.html', {
    'message': 'Signup was success.  Thank you!', 
  }, context_instance=RequestContext(request))