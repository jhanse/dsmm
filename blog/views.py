from django.template.context import RequestContext
from blog.models import *
from projekti.models import *
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import list_detail

def blog_generic_view(request, redirect_to, paginate = True, **view_args):
    view_args['queryset'] = view_args.get('queryset', Post.objects.all())
    view_args['template_object_name'] = 'post'

    if paginate:
        view_args['paginate_by'] = 6

    return redirect_to(request, **view_args)

def page_detail(request, slug):
    return render_to_response('blog/page.html', {
        'page': get_object_or_404(Page, slug=slug),
        'request': request,
    })

def novice_by_projekt(request, avtor_posta):
    try:
        projekt = Projekt.objects.get(author=avtor_posta)
        avtor = projekt.author
    except Projekt.DoesNotExist:
        avtor = avtor_posta
    return blog_generic_view(
        request,
        list_detail.object_list,
        queryset = Post.objects.filter(author=avtor),
    )
