from django.views import View
from django.forms import ModelForm
from ipl.models import *
from django.shortcuts import *
# from onlineapp.forms.college_form import *
# from onlineapp.forms import *
from django.urls import resolve

class HomeView(View):
    def get(self,request,*args,**kwargs):
        if(kwargs):
            matches=matches=Matches.objects.filter(season=kwargs.get("season"))
            return render(
                request,
                template_name="home.html",
                context={
                              "matches":matches,"season":kwargs.get("season")
                        }
                )



# returning default 2019 home page
        matches=Matches.objects.filter(season=2019)
        season=2019
        return render(
            request,
            'home.html',
            {"matches":matches,"season":season}
        )
