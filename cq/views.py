from cq.models import ComedyQuote
from django.http import Http404
from django.shortcuts import render_to_response
import random
from django.template import RequestContext

def home(request):
    quote_list = ComedyQuote.objects.all()
    return render_to_response('cq/home.html', {'quote_list': quote_list})

def detail(request, quote_id):
    try:
        q = ComedyQuote.objects.get(pk=quote_id)
    except ComedyQuote.DoesNotExist:
        raise Http404
    return render_to_response('cq/detail.html', {'quote':q})

def q_random(request):
    q_list = ComedyQuote.objects.all()
    q_list_size = len(q_list)
    ran_num = random.randint(0, q_list_size - 1)
    rand_quote_obj = q_list[ran_num]
    rand_quote = rand_quote_obj.quote
    q_lines = rand_quote.split('\n')
    return render_to_response('cq/random.html', {'quote': q_lines, 'id':
        rand_quote_obj.id},
            context_instance=RequestContext(request))

