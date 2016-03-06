from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from django.utils import timezone


def index(request):
    posts = List.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'myapp/index.html', {'posts': posts})

# Create your views here.
