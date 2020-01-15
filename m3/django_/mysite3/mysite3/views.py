from django.shortcuts import render


def index_view(request):
    lst = ['Beijing','Shanghai','Guangzhou']

    return render(request,'index.html',locals())

def music_view(request):


    return render(request,'music.html')

def sports_view(request):

    return render(request,'sports.html')

def page1_view(request):

    return render(request,'page1.html')

def page2_view(request):

    return render(request,'page2.html')

def pagen_view(request,n):

    return render(request,'pagen.html',locals())

def test_static(request):

    return render(request,'test_static.html')