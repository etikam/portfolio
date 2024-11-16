from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import SkillsForm
from .models import Skills, Projects, CategorieProject, Formation, SoftSkill
from blog.models import Article, Comment

# Create your views here.


def index(request):

    # my skills
    skills = Skills.objects.all()
    # my projects
    projects = Projects.objects.all().order_by("-published_at")
    # categories projects
    projects_categories = CategorieProject.objects.all()
    # traitement du formulaaire d'enregistrement d'une compétence, (à supprimer parce que ça va etre coté administrateur seulement)
    form = SkillsForm()
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,'Compétenses ajoutée avec succès')

    # Récupération des formations suivies
    trainings = Formation.objects.all().order_by("date_completed")

    # Récupération des compétences propres (sofltSkills)
    softskills = SoftSkill.objects.all()

    # Récupération des 5 derniers post du blog
    last_post = Article.objects.all().order_by("date")[:5]

    context = {
        "skills": skills,
        "projects": projects,
        "projets_cat": projects_categories,
        "form": form,
        "trainings": trainings,
        "softskills": softskills,
        "last_post": last_post,
    }
    return render(request, "portfolio/index.html", context)


class SkillCreateView(CreateView):
    model = Skills
    form_class = SkillsForm
    template_name = "portfolio/skills/create_form.html"
    success_url = reverse_lazy("home")


class ProjectDetailView(DetailView):
    model = Projects
    template_name = "portfolio/projets/details.html"
    context_object_name = "project"


def custom_404_view(request, exception=None):
    context = {
        "detail": "Impossible de touver la ressource demander, veuillez venir à la page d'accueil",
        "status": 404,
    }
    return render(request, "portofolio/customs_error_pages/404.html")
