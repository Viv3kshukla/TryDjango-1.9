from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post
def posts_home(request):
    title="Home"
    context={
        'title':title,
    }
    return render(request,'index.html',context)

def posts_create(request):
    title = "Create"
    context = {
        'title': title,
    }
    return render(request, 'index.html', context)

def posts_detail(request):

    return HttpResponse("<h1> Hello Detail</h1>")

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