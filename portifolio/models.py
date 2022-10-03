from hashlib import blake2b

from django.db import models


class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=65)
    sobrenome = models.CharField(max_length=250)
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    foto = models.ImageField(
        upload_to='dev/perfil/', blank=True, default='')

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'


class Projeto(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    link_repositorio = models.CharField(max_length=250)
    link_site = models.CharField(max_length=250, blank=True, null=True)
    capa = models.ImageField(
        upload_to='projeto/capa/', blank=True, default='')
    desenvolvedor = models.ForeignKey(
        Desenvolvedor, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='projetos')

    def __str__(self) -> str:
        return self.titulo


class Habilidade(models.Model):
    SKILLS_CHOICHES = [
        ('HS', 'Hard Skill'),
        ('SS', 'Soft Skill'),
    ]

    nome = models.CharField(max_length=65)
    tipo = models.CharField(max_length=2, choices=SKILLS_CHOICHES)
    link = models.CharField(max_length=250, null=True, blank=True)
    icone = models.CharField(max_length=65, null=True, blank=True)
    desenvolvedor = models.ForeignKey(
        Desenvolvedor, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='habilidades')
    projetos = models.ManyToManyField(
        Projeto, related_name='tecnologias', blank=True)

    def __str__(self) -> str:
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=65)
    link = models.CharField(max_length=250)
    icone = models.CharField(max_length=65, null=True, blank=True)
    desenvolvedor = models.ForeignKey(
        Desenvolvedor, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='contatos')

    def __str__(self) -> str:
        return self.nome
