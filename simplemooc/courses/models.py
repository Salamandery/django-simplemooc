from django.db import models
from simplemooc.courses.manager import CourseManager

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre', blank=True)
    start_date = models.DateField('Data de inicio', blank=True, null=True)
    image = models.ImageField(
        verbose_name='Imagem', 
        blank=True, null=True,
        upload_to='courses/images', 
    )

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']