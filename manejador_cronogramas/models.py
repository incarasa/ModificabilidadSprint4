from django.db import models

class Cronograma(models.Model):
    nombre = models.CharField(max_length=50)
    estudiantes = models.ManyToManyField(  # Relación muchos a muchos
        'Estudiante', 
        related_name='cronogramas'  # Nombre único para acceder desde Estudiante
    )

    def __str__(self) -> str:
        return str(self.nombre)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    documento = models.CharField(max_length=50)
    curso = models.CharField(max_length=15)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return str(self.nombre)


class Pago(models.Model):
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)  # Relación a Cronograma
    mes = models.IntegerField()
    meses = models.CharField(max_length=3)
    valor = models.IntegerField()
    fecha_evento = models.DateField(null=True, blank=True)
    intereses = models.IntegerField()

    def __str__(self) -> str:
        return str(self.meses)