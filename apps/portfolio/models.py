from django.db import models
from django.db.models.query import QuerySet
from django.db.models.signals import pre_save
from django.utils import timezone

from apps.portfolio.utils import unique_slug_generator

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name='Categoria',
        max_length=250,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name


class Project(models.Model):

    class ProjectObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='published')

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        default=1
    )

    name = models.CharField(
        verbose_name='Nombre del proyecto',
        max_length=250,
        unique=True
    )

    slug = models.SlugField(
        verbose_name='Slug',
        max_length=250,
        unique_for_date='published',
        null=True,
        blank=True,
        unique=True
    )

    published = models.DateTimeField(
        verbose_name='Fecha de publicacion',
        default=timezone.now
    )

    description = models.TextField(
        verbose_name='Descripcion'
    )

    image = models.ImageField(
        verbose_name='Imagen de proyecto',
        upload_to='projects',
        null=True,
        blank=True
    )

    options = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )
    status = models.CharField(
        verbose_name='Estado del post',
        max_length=10,
        choices=options,
        default='draft'
    )

    github = models.CharField(
        verbose_name='Link al proyecto en git',
        max_length=250,
        unique=True,
        blank=True,
        null=True
    )

    objects = models.Manager()
    projectobjects = ProjectObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self) -> str:
        return self.name
    
def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Project)