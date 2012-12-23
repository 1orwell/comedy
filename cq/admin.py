from cq.models import ComedyQuote
from django.contrib import admin

class ComedyQuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'source')
    list_filter = ['source', 'tv_series']

admin.site.register(ComedyQuote, ComedyQuoteAdmin)
