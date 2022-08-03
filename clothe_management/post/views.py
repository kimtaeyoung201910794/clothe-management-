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



def postFormInput(request):
    return render(request,"post/add.html")

def add(request):
    if request.method == "POST":
        print()
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.views = 0
            if []:
                print(1)
            new_post.annonymous = True if len(request.POST.getlist("annonymous"))!=0 else False
            new_post.image = request.FILES['image']
            new_post.user = myUser.objects.get(id=request.user.id)

            new_post.save()
    
            return redirect('boards')

    return render(request, 'post/add.html')
    
def boards(request):
    datas = Post.objects.all()
    posts = list(datas)

    context = {
        'time' : time(),
        'posts' : posts
    }
    return render(request,'post/board.html',context)