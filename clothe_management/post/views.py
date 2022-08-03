from django.shortcuts import render, redirect
from .forms import PostForm
from account.models import myUser
from .models import Post
from datetime import datetime,timedelta

# Create your views here.
def time():
    datas = Post.objects.all().order_by('-time')[0:6]
    return list(datas)
def main(request):
    
    context = {
        'time' : time()
    }
    return render(request, 'post/main.html',context)



def postFormInput(request,type):
    context = {
        'title' : type,
        'time' : time(),
    }
    return render(request,"post/add.html",context)

def add(request,type):
    context = {
        'title' : type,
        'time' : time(),
    }
    if request.method == "POST":
        print(request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.views = 0
            new_post.annonymous = True if request.POST.getlist("annonymous[]") else False
            new_post.image = request.FILES['image']
            new_post.user = myUser.objects.get(id=request.user.id)

            new_post.save()
    
            return render(request,'post/board.html',context)
    
    return render(request, 'post/add.html',context)
    
def boards(request,type):
    datas = Post.objects.filter(board=type)
    posts = list(datas)

    context = {
        'title' : type,
        'time' : time(),
        'posts' : posts
    }
    return render(request,'post/board.html',context)

def detail(request,type,post_id):
    post = Post.objects.get(id = post_id)
    post.views+=1
    post.save()
    context = {
        'title' : type,
        'time' : time(),
    }
    return render(request,'post/detail.html',context)