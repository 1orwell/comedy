from django.db import models

class Season(models.Model):
    number = models.IntegerField()
    def __unicode__(self):
        return str(self.number)

class Episode(models.Model):
    number = models.IntegerField()
    air_date = models.DateTimeField('air date', blank=True, null=True)
    season = models.ForeignKey(Season)
    name = models.CharField(max_length=100)
    video_link = models.CharField("Video link", max_length=500, blank=True)
    plot = models.TextField()
    def __unicode__(self):
        ret_val = 'series: ' + str(self.season) + ', episode: ' + str(self.number)
        return ret_val

