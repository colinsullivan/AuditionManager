from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

from auditionapp.productions.models import Production


class Actor(models.Model):
    """An Actor or Actress"""
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    AGE_CHOICES = (
      (0, '1-6'),
      (1, '7-12'),
      (3, '13-18'),
      (4, '19-30'),
      (5, '31-45'),
      (6, '45+')
    )
    age_range = models.IntegerField(max_length=1, choices=AGE_CHOICES)
    height = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    union = models.CharField(max_length=128)
    special = models.TextField(blank=None)
    reference = models.TextField(blank=None)
    line1 = models.CharField(max_length = 128)
    line2 = models.CharField(max_length = 128, blank=True)
    city = models.CharField(max_length = 128)
    state = USStateField()
    zipcode = models.CharField(max_length=10)
    phone = PhoneNumberField()
    alt_phone = PhoneNumberField(blank=True)
    email = models.EmailField()    


    def __unicode__(self):
        return self.first_name+' '+self.last_name

    @models.permalink
    def get_absolute_url(self):
        return ('Actor', [self.id])

class Audition(models.Model):
    """An audition by someone"""
    production = models.ForeignKey(Production)
    actor = models.ForeignKey(Actor)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
    

    

    def __unicode__(self):
      return str(self.actor)+' on '+str(self.date)
    
    def notes_excerpt(self):
      notes = self.notes
      if len(notes) > 50:
        # Return first 47, plus '...'
        return notes[:47]+'...'
      else:
        return notes

    @models.permalink
    def get_absolute_url(self):
        return ('Actor', [self.id])
