from django.db import models
import uuid

# Create your models here.


class Skills(models.Model):
    label = models.CharField(max_length=150)
    level = models.IntegerField()

    def __str__(self):
        return self.label


class Technologies(models.Model):
    name = models.CharField(max_length=50)
    # image = models.ImageField(upload_to="image-technologie", verbose_name="une image un un logo representant la technologie")

    def __str__(self) -> str:
        return self.name


class CategorieProject(models.Model):
    label = models.CharField(max_length=50)
    image = models.ImageField(upload_to="categori-images")

    def __str__(self) -> str:
        return self.label


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    technologies = models.ManyToManyField(Technologies, related_name="technologies")
    categories = models.ForeignKey(
        CategorieProject, on_delete=models.CASCADE, related_name="categories"
    )
    image = models.ImageField(upload_to="project-cover")
    url = models.URLField(max_length=200, blank=True, null=True)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(
        max_length=20, default=1
    )  # 1 ==  en cours, 2 == realisé, 3 == En production

    def __str__(self) -> str:
        return self.title


class ImageProject(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="image-project")
    catption = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="une brève description de l'image (facultatif)",
    )
    projet = models.ForeignKey(
        Projects, on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self) -> str:
        return f"{self.uid}"


class Formation(models.Model):
    label = models.CharField(max_length=100, verbose_name="Intitulé de la formation")
    trainer = models.CharField(max_length=100, verbose_name="Institution")
    duration = models.CharField(
        max_length=50, verbose_name="Durée de la formation"
    )  # Ex: '3 mois', '6 semaines'
    date_started = models.DateField(null=True, blank=True, verbose_name="Date de debut")
    date_completed = models.DateField(
        null=True, blank=True, verbose_name="Date d'achèvement"
    )
    certificate = models.FileField(
        upload_to="certificates/", null=True, blank=True, verbose_name="Certificat"
    )

    def __str__(self):
        return f"{self.label} - {self.trainer}"


class SoftSkill(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.label
