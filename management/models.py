from django.db import models
from django.conf import settings # Importe settings para o usuário

class TipoAnimal(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Tipo")
    icone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Classe do Ícone")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Raca(models.Model):
    tipo_animal = models.ForeignKey(TipoAnimal, on_delete=models.PROTECT, related_name='racas')
    nome = models.CharField(max_length=100, verbose_name="Nome da Raça")
    observacoes_manejo = models.TextField(blank=True, verbose_name="Observações de Manejo")
    ativo = models.BooleanField(default=True)

    class Meta:
        # Garante que não haja duas raças com o mesmo nome para o mesmo tipo de animal
        unique_together = ('tipo_animal', 'nome')

    def __str__(self):
        return f"{self.nome} ({self.tipo_animal.nome})"

class Animal(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]

    proprietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    # VERIFIQUE SE ESTE CAMPO ESTÁ AQUI E SALVO
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    tipo_animal = models.ForeignKey(TipoAnimal, on_delete=models.PROTECT)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def get_sexo_icone(self):
        if self.sexo == 'M':
            return 'fas fa-mars'
        elif self.sexo == 'F':
            return 'fas fa-venus'
        return ''