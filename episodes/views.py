from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Season


def series_list(request):
    series_list = Season.objects.all()
    return render_to_response('episodes/list.html', {'series_list':series_list},
        context_instance=RequestContext(request))
