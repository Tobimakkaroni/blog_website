from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .models import Post
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

def rust_calculator_view(request):
    return render(request, 'rust/rust_calculator.html')