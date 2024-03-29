from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.utils import timezone
import time
import pdb


def home(request):
    context = {"posts": Post.objects.all().order_by("-date_posted")}
    return render(request, "blog/home.html", context)


def finish_study(request):

    from utils.make_a_new_blog_post import make_a_post
    time_finished = int(round(time.time()))
    points_earned = time_finished - request.session["start_time"]
    time_studied = int(points_earned / 60) 
    request.session["user_description"] = request.POST["user_description"]
    if request.session["user_description"] == "": 
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        request.session["user_description"] = "Session at " + current_time
    make_a_post(
        start_date=timezone.now(),
        time_studied=time_studied,
        points_earned=points_earned,
        user=request.user,
        user_description=request.session["user_description"],
    )

    # 1 second = 1 wallet point
    profile = request.user.profile
    profile.wallet_points = request.user.profile.wallet_points + time_studied
    profile.save()

    return home(request)


def map(request):
    return render(request, "blog/map.html")


def study(request):
    request.session["start_time"] = int(round(time.time()))
    request.session["user_description"] = ""
    return render(request, "blog/settfime.html")


def rewards(request):
    return render(request, "blog/rewardsnew.html")


def tutorial(request):
    return render(request, "blog/Tutorial.html")


def onboarding(request):
    return render(request, "blog/onboarding.html")


def save_profile(request):
    if request.POST:
        request.session["first_name"] = request.POST["FirstName"]
        request.session["second_name"] = request.POST["LastName"]
        return render(request, "blog/onboarding_universities.html")

    return render(request, "blog/onboarding_universities.html")


def store_time(request):
    if request.POST:
        session_length_string = request.POST["sessionlength"]
        minutes = session_length_string[:2]
        seconds = session_length_string[-2:]
        request.session["initial_time_string"] = request.POST["sessionlength"]
        request.session["study_time"] = (int(minutes) * 60 * 1000) + (
            int(seconds) * 1000
        )

    return render(request, "blog/Timer.html")


def save_uni(request):
    if request.POST:
        request.session["university"] = request.POST["university"]
        return render(request, "blog/onboarding_subject.html")

    return render(request, "blog/onboarding_subject.html")


def save_subject(request):
    if request.POST:
        request.session["subject"] = request.POST["subject"]
        return render(request, "blog/finish_onboarding.html")

    return render(request, "blog/finish_onboarding.ht ml")


def make_a_code(request):
    return render(request, "blog/make_a_code.html")


def purchase_rewards_100(request):
    profile = request.user.profile
    profile.wallet_points = request.user.profile.wallet_points - 10
    profile.save()

    return home(request)


def purchase_rewards_500(request):
    profile = request.user.profile
    profile.wallet_points = request.user.profile.wallet_points - 50
    profile.save()

    return home(request)


def purchase_rewards_50(request):
    profile = request.user.profile
    profile.wallet_points = request.user.profile.wallet_points - 50
    profile.save()

    return home(request)

def load_user_post_stats():
    posts = Post.objects().all()
    return posts


class PostListView(ListView):
    model = Post
    template_name = "blog/landing.html"  
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
