from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'main/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Aquí asignamos el usuario autenticado a la publicación
            post.save()
            return redirect('index')  # Redirige a la página principal después de crear la publicación
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})
