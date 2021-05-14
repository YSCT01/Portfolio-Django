from django.db import models

# Create your models here.
class Proyecto(models.Model):
    proyecto = models.CharField(max_length=255, null=False)
    descripcion = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=255, null=False)
    tecnologias = models.CharField(max_length=255, null=False)
    ano = models.IntegerField(null=False)
    imagen = models.ImageField(default='null', upload_to='Proyectos')
    urlimg = models.CharField(max_lenght=255, null=False)

    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
    #End Meta

    def __str__(self):
        return self.proyecto
    #End __str__

#End Proyecto