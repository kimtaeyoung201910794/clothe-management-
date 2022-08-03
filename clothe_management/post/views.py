from django.shortcuts import render, redirect
from .forms import PostForm
from account.models import myUser
from .models import Post
from datetime import datetime

# Create your views here.
def main(request):
    datas = Post.objects.all().order_by('-time')[0:6]
    time = list(datas)
    context = {
        'time' : time
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
            new_post.annonymous = True if request.POST.getlist("annonymous") else False
            new_post.image = request.FILES['image']
            new_post.user = myUser.objects.get(id=request.user.id)

            new_post.save()
    
            return redirect('boards')

    return render(request, 'post/add.html')
    
def boards(request):
    datas = Post.objects.all()
    posts = []
    for data in datas:
        print(data.time)
        time = datetime.strptime(data.time,'%Y-%m-%d %H:%M:%S')-datetime.strptime(datetime.now(),'%Y-%m-%d %H:%M:%S')
        print(time)
    #     # posts.append({
    #     #     'title':data.title,
    #     #     'content':data.content,
    #     #     'time':
    #     # })
    # context = {
    #     'posts' : posts
    # }
    return render(request,'post/board.html')