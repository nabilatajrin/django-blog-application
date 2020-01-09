from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import BlogPost

# Create your views here.


def blog_post_detail_page(request, slug):
    #obj = BlogPost.objects.get(id=post_id)
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)