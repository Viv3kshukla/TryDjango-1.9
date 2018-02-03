from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Post

def posts_create(request):
    title = "Create"
    context = {
        'title': title,
    }
    return render(request, 'index.html', context)

def posts_detail(request,id=None):
    title="Detail"
    # instance = Post.objects.get(id=1)
    instance=get_object_or_404(Post,id=id)
    context={
        'title':instance.title,
        'instance':instance,

    }
    return render(request, 'post_detail.html', context)

def posts_list(request):
    title="ListView"
    queryset=Post.objects.all()

    context = {
        'object_list':queryset,
        'title':title,
    }
    # if request.user.is_authenticated():
    #     context = {
    #         'title':'My User List',
    #     }
    # else:
    #     context = {
    #         'title':'List'
    #     }
    return render(request, 'index.html', context)

def posts_update(request):

    return HttpResponse("<h1> Hello Update</h1>")

def posts_delete(request):

    return HttpResponse("<h1> Hello Delete</h1>")