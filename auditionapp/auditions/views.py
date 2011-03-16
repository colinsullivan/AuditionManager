from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from auditions.forms import ActorSignupForm
from auditions.models import Actor
from django.core.files.base import ContentFile



# This view allows actors to sign up.
def actorsignup(request):
  
  if request.method == 'POST':
    signupForm = ActorSignupForm(request.POST)
    
    if signupForm.is_valid():
      # Create actor
      actor = signupForm.save()
      
      # Forward to photo view
      return HttpResponseRedirect('/actorphoto/'+str(actor.id))

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
  
# This view is used to take a photo of the actor
# @param  {Number}  actor_id  - The id of the actor who is taking the picture
@csrf_exempt
def actorphoto(request, actor_id):
  
  if request.method == 'POST':
    actor = Actor.objects.get(pk=actor_id)
    
    filename = 'actor-'+actor_id+'_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.jpg'
    
    actor.image.save(filename, ContentFile(request.raw_post_data))
    
    # Return a 200
    return HttpResponse()
  else:
    message = 'Please take a photo of yourself.'
  
  return render_to_response('actor_photo.html', {
    'message': message,
    'actor_id': actor_id, 
  }, context_instance=RequestContext(request))

# This is the view that is used when the actor signup was a success
def actorsignupsuccess(request):
  
  return render_to_response('actor_signup_success.html', {
    'message': 'Signup was success.  Thank you!', 
  }, context_instance=RequestContext(request))