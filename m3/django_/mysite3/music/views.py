from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'music/index.html')
    # return HttpResponse('this is index of music')