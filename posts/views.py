from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from .models import Post
from .forms import PostForm

def posts_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        print(form.cleaned_data)
        instance.save()
        # message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)

def posts_detail(request,id=None):
    title="Detail"

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
    return render(request, 'index.html', context)

def posts_update(request,id=None):

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # message success
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form':form,
    }
    return render(request, 'post_form.html', context)

def posts_delete(request):

    return HttpResponse("<h1> Hello Delete</h1>")