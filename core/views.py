from msilib.schema import ListView
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import AboutUs


class About(ListView):
    model = AboutUs
    template_name ='core/about.html'
    context_object_name = "aboutus"


class Main(TemplateView):
    template_name =  'core/main.html'
    # extra_context = {'title': 'bilim'} 

def core(request):
    return HttpResponse('test')


class LoginView(TemplateView):
    template_name = "core/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class ProfilePage(TemplateView):
   template_name = "core/profile.html"
# def profile(request):
#     user = request.user
#     profile_object = user.profile
#     return render(request, 'core/profile.html',{'profile_1': profile_object})


class RegisterView(TemplateView):
    template_name = "core/registration.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))
                # return HttpResponse('успешно зарегистрировались')
        return render(request, self.template_name)