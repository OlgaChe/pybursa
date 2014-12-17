from django.db import models


class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=25, blank=True)
    region = models.CharField(max_length=25, blank=True)
    street = models.CharField(max_length=25)
    house = models.CharField(max_length=5)

    def __unicode__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.zip_code, self.country, self.state, self.region, self.street, self.house)
