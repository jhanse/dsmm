from projekti.models import Projekt
from blog.models import Post
from imagestore.models import Album
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    projekt_list = Projekt.objects.all().order_by('ime')
    return render_to_response('projekti/projekt_seznam.html', {
        'projekt_list': projekt_list,
        'request': request,
    })

def detail(request, slug):
    projekt_detail = get_object_or_404(Projekt, slug=slug)
    owner = projekt_detail.author_id
    galerije = Album.objects.filter(user=owner)
    posts_by = Post.objects.filter(author=owner)
    return render_to_response('projekti/projekt_detail.html', {
        'projekt': projekt_detail,
        'galerije': galerije,
        'posts_by': posts_by,
        'request': request,
    })