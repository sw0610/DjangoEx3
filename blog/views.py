from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import PostForm  #forms.py에서 PostForm 가져오기

# Create your views here.
def main(request):
    posts = Post.objects #Post.objects 를 post 변수에 담기
    return render(request, 'posts.html',{'posts':posts})#인자 3개: request,template, context

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm()        
    return render(request, 'create.html',{'form',form})

def detail(request, pk):
    post=get_object_or_404(Post,pk=pk)#해당 객체가 있으면 가져오고 없으면 404 에러, pk로 pk사용
    return render(request,'detail.html',{'post':post})

def update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = PostForm(instance=post)
    return render(request,'update.html', {'form',form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('main')
