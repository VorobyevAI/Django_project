from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


class NewsUpdate(DetailView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDetail(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def posts(request):
    model = Articles.objects.all()
    return render(request, 'news/posts.html', {'model' : model})


def create(request):
    error = ''

    if request.method == 'POST':
        model = ArticlesForm(request.POST)
        if model.is_valid():
            model.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    dat = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', dat)



