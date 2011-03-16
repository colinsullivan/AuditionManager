from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class ProductionType(models.Model):
    """A type of production"""
    name = models.CharField(max_length=128,help_text="Enter the name for this production type.")

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('ProductionType', [self.id])

class Production(models.Model):
    """Something that someone can apply for"""
    name = models.CharField(max_length=128)
    production_type = models.ForeignKey(ProductionType, help_text="Please select the type of production")
    default_production = models.BooleanField(help_text = "When set to true, this production will be the default for all new auditions.")
    
    def save(self, *args, **kwargs):
      
      # If the default_production variable is being set to true
      if self.default_production is True:
        try:
          # Get current production that is set as default production
          currentDefault = Production.objects.get(default_production = True)

          # If it is not ourself
          if currentDefault.pk is not self.pk:
            # Set it to false and save
            currentDefault.default_production = False
            currentDefault.save()
        except ObjectDoesNotExist, e:
          # No previous default, no need to do anything
          pass

      
      return super(Production, self).save(*args, **kwargs)

    

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('Production', [self.id])
