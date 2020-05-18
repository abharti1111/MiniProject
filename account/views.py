from django.shortcuts import render
from django.views.generic import ( DetailView, 
                                TemplateView, 
                                FormView, 
                                CreateView, 
                                UpdateView, 
                                ListView,

                                )
from .models import PoliceStationProfile
# from django.
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
class PoliceStationView(DetailView):
    template_name = 'account/policestation.html'
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.request.user.username)



class HomePageView(TemplateView):
    template_name = 'account/dashboard.html'
    
class AboutUsPageView(TemplateView):
    template_name = "account/about.html"

class ContactsPageView(TemplateView):
    template_name = "account/contact.html"

