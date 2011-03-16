from django.db import models

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
    prodType = models.ForeignKey(ProductionType, help_text="Please select the type of production")

    

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('Production', [self.id])
