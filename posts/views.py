from django.shortcuts import render
from django.http import HttpResponse 
# from .models import Post

# Create your views here.

def index(request):
    # post = Post.objrcts.order_by('-created_at')[:3]
    # context = {'post' : post}
    # return render(request, 'posts/index.html', context)
    return HttpResponse('HELLO')