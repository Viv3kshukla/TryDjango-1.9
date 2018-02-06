from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
# Create your views here.
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
from .forms import PostForm

def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise Http404

    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        print(form.cleaned_data)
        instance.save()
        # message success
        messages.success(request,"successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)

def posts_detail(request,slug=None):
    title="Detail"

    instance=get_object_or_404(Post,slug=slug)
    context={
        'title':instance.title,
        'instance':instance,

    }
    return render(request, 'post_detail.html', context)

def posts_list(request):
    title="ListView"
    queryset_list=Post.objects.all().order_by("-timestamp")
    paginator=Paginator(queryset_list,5)
    page_request_var="page"
    page=request.GET.get(page_request_var)
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)

    context = {
        'object_list':queryset,
        'title':title,
        'page_request_var':page_request_var,
    }
    return render(request, 'posts_list.html', context)

def posts_update(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # success message
        messages.success(request, "successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': instance.title,
        'instance': instance,
        'form':form,
    }
    return render(request, 'post_form.html', context)

def posts_delete(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "successfully deleted")
    return redirect("posts:list")