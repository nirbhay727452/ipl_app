from django.views import View
from django.forms import ModelForm
from ipl.models import *
from django.shortcuts import *
# from onlineapp.forms.college_form import *
# from onlineapp.forms import *
from django.urls import resolve

class MatchView(View):
    def get(self,request,*args,**kwargs):
        if(kwargs):
            matches=Deliveries.objects.filter(match_id=kwargs.get("match_id"))
            return render(
                request,
                template_name="match.html",
                context={
                              "matches":matches,
                        }
                )


