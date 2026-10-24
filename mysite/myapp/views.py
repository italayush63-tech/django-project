from django.shortcuts import redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'myapp/home.html' , {'name': 'ayush ital'})

def about(request):
    return render(request, 'myapp/about.html')

@login_required(login_url='/login/')
def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html' , {'form': form, 'success': success})            

def posts(request):
    all_posts = Post.objects.all().order_by('-created')
    return render(request, 'myapp/posts.html', {'posts': all_posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'myapp/post_detail.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})