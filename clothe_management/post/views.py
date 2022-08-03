from django.shortcuts import render, redirect
from .forms import PostForm
from account.models import myUser
from .models import Post

# Create your views here.
def main(request):
    datas = Post.objects.all().order_by('-time')[0:6]
    time = list(datas)
    print(time)
    context = {
        'time' : time
    }
    return render(request, 'post/main.html',context)



def postFormInput(request):
    return render(request,"post/add.html")

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.views = 0
            new_post.image = request.FILES['image']
            new_post.user = myUser.objects.get(id=request.user.id)

            new_post.save()
    
            return redirect('boards')

    return render(request, 'post/add.html')
    
def boards(request):
    return render(request,'post/board.html')