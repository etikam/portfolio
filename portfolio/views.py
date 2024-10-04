from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SkillsForm
from .models import Skills


# Create your views here.

def index(request):
    
    #my skills
    skills = Skills.objects.all()
    context ={
        'skills':skills
    }
    return render(request,'portfolio/index.html',context)


class SkillCreateView(CreateView):
    model = Skills
    form_class = SkillsForm
    template_name = "portfolio/skills/create_form.html"
    success_url = reverse_lazy("home")
    