from django.shortcuts import render

# Create your views here.
def chatting(request):
    return render(request, 'chat/main.html')