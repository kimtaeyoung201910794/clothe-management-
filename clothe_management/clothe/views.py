from django.shortcuts import render, redirect
from account.models import myUser
from clothe.models import clothe
from .forms import clotheForm

def search(request):
    clothes = []
    if request.method=='POST':
        userid = request.POST.get('username')
        keyward = request.POST.get('keyward')
        datas = clothe.objects.filter(name__contains = keyward)
        for data in datas:
            clothes.append(data.image.url)
        return render(request, 'list/search.html',{'userid':userid,'keyward':keyward, 'clothes':clothes})

def add(request):
    
    if request.method == "POST":
        form = clotheForm(request.POST)
        if form.is_valid():
            new_clothe = form.save(commit=False)
            new_clothe.image = request.FILES['image']
            new_clothe.user = myUser.objects.get(id='2')

            new_clothe.save()

            return redirect('home')

    return render(request,'clothe/add.html')
