from django.db import models

from django.contrib.localflavor.us.models import USStateField

from auditionapp.productions.models import Production



class Address(models.Model):
    """An address for an actor"""
    line1 = models.CharField(max_length = 128)
    line2 = models.CharField(max_length = 128, blank=True)
    city = models.CharField(max_length = 128)
    state = USStateField()
    zipcode = models.CharField(max_length=10)
    latitude = models.DecimalField(decimal_places=7, max_digits=128)
    longitude = models.DecimalField(decimal_places=7, max_digits=128)
    actor = models.ForeignKey('Actor')

    

    def __unicode__(self):
        return u"Address"

    @models.permalink
    def get_absolute_url(self):
        return ('Address', [self.id])

class Actor(models.Model):
    """An Actor or Actress"""
    name = models.CharField(max_length=128)

    

    def __unicode__(self):
        return u"Actor"

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
        return u"Actor"

    @models.permalink
    def get_absolute_url(self):
        return ('Actor', [self.id])
