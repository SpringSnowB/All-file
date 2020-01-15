from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'book/index.html')
    # return HttpResponse('this is index of book')


def add_view(request):
    if request.method == 'GET':
         return render(request,'book/add.html')
    elif request.method == 'POST':
        btn = request.POST['show']