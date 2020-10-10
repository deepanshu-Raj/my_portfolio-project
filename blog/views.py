from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request,'blog/blog-home.html',{'blogs' : blogs})
