from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Season
from models import Episode
from cq.views import format_quote
from django.http import Http404


def series_list(request):
    series_list = Season.objects.all()
    return render_to_response('episodes/list.html', {'series_list':series_list},
        context_instance=RequestContext(request))

def detail(request, episode_id):
    try:
        e = Episode.objects.get(pk=episode_id)
        if e.id <= 23:
            next_ep = e.id + 1
            if next_ep == 24:
                next_ep = 1
    except Episode.DoesNotExist:
        raise Http404
    return render_to_response('episodes/detail.html', {'episode': e, 'next_ep':
        next_ep},
        context_instance=RequestContext(request))
    

