from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'meus_posts/lista_posts.html', {'posts': posts})

@login_required
def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'meus_posts/form_post.html', {'form': form})
