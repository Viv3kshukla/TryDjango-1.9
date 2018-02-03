from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Post
from .forms import PostForm

def posts_create(request):
    form=PostForm(request.POST or None)      # either grab that form data or do nothing
    if form.is_valid():
        instance=form.save(commit=False)
        print(form.cleaned_data)             # printing out form data
        instance.save()
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)

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