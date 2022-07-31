from django.shortcuts import render
from .models import Articles

def posts(request):
    model = Articles.objects.all()
    return render(request, 'news/posts.html', {'model' : model})


