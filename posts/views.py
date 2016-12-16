from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone
from posts.models import Post
from posts.form import PostForm
from django.http.response import HttpResponseRedirect

def post_list(request):
    queryset = Post.objects.all()
    context = {'posts': queryset}  #.order_by("-timestamp")

    return render(request, 'post_list.html', context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj= form.save(commit=False)
        obj.save()    
        return redirect('list')
    context = {'form': form}
    return render(request, 'post_form.html', context)

def post_detail(request, slug=None):
    obj = get_object_or_404(Post, slug=slug)
    context = {'post': obj}
    return render(request, 'post_detail.html', context)

def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'post': instance, 'form':form}
    return render(request, 'post_form.html', context)

def post_delete(request):pass