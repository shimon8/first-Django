from django.http import HttpResponse
from .models import Album
from django.template import loader
from django.http import Http404
def index(req):
    albums = Album.objects.all()
    html = ''
    template = loader.get_template('music/index.html')
    context = {
        'albums': albums, }
    return HttpResponse(template.render(context, req))
def detailes(req, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except:
        return Http404("album not found")
    return HttpResponse(loader.get_template('music/detail.html').render({"album": album}, req))
def favoraite(req,album_id):
    return 
