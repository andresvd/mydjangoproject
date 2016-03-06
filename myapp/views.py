from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from django.utils import timezone
from .forms import PostList


def index(request):
    posts = List.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'myapp/index.html', {'posts': posts})

def post_new(request):
    form = PostList()
    return render(request, 'myapp/post_edit.html', {'form': form})
# Create your views here.
