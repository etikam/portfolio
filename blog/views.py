from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import Article, Category, Comment
from blog.forms import CommentForm

# Create your views here.


# Liste des post
class PostListView(generic.ListView):
    model = Article
    template_name = "portfolio/blog/post/all_posts.html"
    queryset = Article.objects.all().order_by("-date")
    paginate_by = 10
    context_object_name = "posts"


# Details post
class PostDetails(generic.DetailView):
    model = Article
    template_name = "portfolio/blog/post/details_post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["form"] = CommentForm()
        return context

    def post(self, request, **kwargs):

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)
            comment.article = self.object
            comment.user = request.user
            comment.save()

            # Redirection après validation du commentaire
            return redirect(reverse("blog:blog_details", kwargs={"pk": self.object.pk}))
        else:
            # Si le formulaire n'est pas valide, renvoyer les erreurs dans le contexte
            context = self.get_context_data(**kwargs)
            context["form"] = form  # Le formulaire avec les erreurs
            return self.render_to_response(context)
