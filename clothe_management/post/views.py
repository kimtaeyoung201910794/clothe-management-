from django.shortcuts import render, redirect
from .forms import PostForm
from account.models import myUser

# Create your views here.
def main(request):

    return render(request, 'post/main.html')

def postFormInput(request):
    return render(request,"post/add.html")

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.image = request.FILES['image']
            new_post.user = myUser.objects.get(id=request.user.id)

            new_post.save()

            return redirect('boards')

    return render(request, 'post/board.html')
    
def boards(request):
    return render(request,'post/board.html')