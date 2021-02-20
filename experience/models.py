from django.db import models

# Create your models here.
class Experience(models.Model):
    empresa = models.CharField(max_length=255, null=False)
    tiempo = models.IntegerField(max_length=10, null=False)

    # Information in admin panel
    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
    # End Class Meta

    #Nombre en panel
    def __str__(self):
        return self.empresa
    #End function __str__

#End Experience

class Lenguajes(models.Model):
    lenguaje = models.CharField(max_length=255, null=False)
    habilidad = models.IntegerField(max_length=100, null=False)

    class Meta:
        verbose_name="Lenguaje"
        verbose_name_plural="Lenguajes"
    #End class Meta

    def __str__(self):
        return self.lenguaje
    #End def __str__

#End Lenguajes