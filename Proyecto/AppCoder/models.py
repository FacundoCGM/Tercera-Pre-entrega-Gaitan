from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NuevoBlog(models.Model):
    tematica = (
    ('politica','Politica'),
    ('deportes', 'Deportes'),
    ('naturaleza','Naturaleza'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    tematica = models.CharField(max_length=15, choices=tematica, default='politica')
    texto = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    emailContacto = models.EmailField()
    imagenBlog = models.ImageField(null=True, blank=True, upload_to="media/imagenesBlog")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
