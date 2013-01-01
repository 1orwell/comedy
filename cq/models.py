from django.db import models
from episodes.models import Episode

class ComedyQuote (models.Model):
    quote = models.TextField()
    TV = 'TV'
    BOOK = 'BK'
    FILM = 'FM'
    UNKNOWN = 'UN'
    source_choices = (
                (TV, 'TV'),
                (BOOK, 'Book'),
                (FILM, 'Film'),
                (UNKNOWN, 'Unknown'),
    )
    source = models.CharField(max_length=2, 
                                choices = source_choices,
                                default = TV)
    tv_series = models.CharField("TV series", max_length=200, blank=True)
    tv_episode = models.CharField("TV episode", max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    video_link = models.CharField("Video link", max_length=500, blank=True)
    pub_date = models.DateTimeField('date published')
    episode = models.ForeignKey(Episode)
    def __unicode__(self):
        return self.quote


    
