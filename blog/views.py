from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .models import Post
from .models import Feature
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SignUpForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django_ratelimit.decorators import ratelimit
from django_comments_xtd.models import XtdComment
from django_comments_xtd.forms import XtdCommentForm
from django.http import Http404

def feature_list(request):
    features = Feature.objects.all()
    print(f'here is my feature list {features}')
    return render(request, 'blog/post_list.html', {'features': features})

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect(reverse_lazy('login'))

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # success
                return redirect('post_list')
            else:
                return render(request, 'registration/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('post_list')

    
@ratelimit(key='ip', rate='5/m', block=True)
@require_POST
@csrf_exempt
def my_view(request):
    return render(request, 'my_template.html')

def post_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        if post_id is None:
            raise Http404("Post ID not found in request.")
        
        post = get_object_or_404(Post, pk=post_id)
        
        form = XtdCommentForm(data=request.POST, target_object=post)
        if form.is_valid():
            comment = form.get_comment_object()
            comment.save()
    else:
        raise Http404("Invalid request method.")

    return render(request, 'your_template.html', {'form': form})

def legal_notice_view(request):
    return render(request, 'blog/legal_notice.html')