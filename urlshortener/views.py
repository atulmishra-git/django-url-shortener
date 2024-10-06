from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .forms import URLShortenerForm
from .serializers import URLSerializer
from .models import URL


def url_view(request):
    template_name = "index.html"
    context = {}
    context['form'] = URLShortenerForm()
    if request.method == "POST":
         form = URLShortenerForm(request.POST)
         if form.is_valid():
            shortened_object = form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            url = shortened_object.url
            context['short_url']  = new_url
            context['url'] = url
            return render(request, template_name, context, status=201)
         else:
            context['errors'] = form.errors
            return render(request, template_name, context, status=400)
    return render(request, template_name, context, status=200)


def redirect_url_view(request, short_url):
    try:
        shortener = URL.objects.get(short_url=short_url)    
        return HttpResponseRedirect(shortener.url)
    except:
        raise Http404('Sorry this link is broken :(')


class URLViewSet(ModelViewSet):
     queryset = URL.objects.all()
     serializer_class = URLSerializer
