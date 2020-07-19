from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'account/index.html'
    ordering = ['-post_date']


class ArticleView(DetailView):
    model = Post
    template_name = 'account/blog_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'account/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'account/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'account/delete_post.html'
    success_url = reverse_lazy('home')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Exists!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                                last_name=last_name)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password does not match!!')
            return redirect('register')

    else:
        return render(request, 'account/register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password does not exists !!')
            return redirect('login')

    else:
        return render(request, 'account/login.html')


def logout(request):

    auth.logout(request)
    return redirect('/')
