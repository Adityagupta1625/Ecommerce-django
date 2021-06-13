from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):
    blog=Blogpost.objects.all()
    params={'blog':blog}
    return render(request,'blog/index.html',params)

def blogPost(request,myid):
    blog=Blogpost.objects.filter(post_id=myid)
    return render(request,'blog/blogPost.html',{'blog':blog[0]})



