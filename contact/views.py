from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin



class ContactTemplateView(TemplateView):
    template_name ='contact/contacts.html'
    

class ContactView(View):
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    
# Create your views here.

