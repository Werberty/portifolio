from django.shortcuts import render

from .models import Contato, Desenvolvedor, Habilidade, Projeto


def home(request):
    desenvolvedor = Desenvolvedor.objects.first()
    projetos = Projeto.objects.all()
    hard_skills = Habilidade.objects.filter(tipo='HS')
    soft_skills = Habilidade.objects.filter(tipo='SS')
    contatos = Contato.objects.all()

    return render(request, 'portifolio/index.html', context={
        'desenvolvedor': desenvolvedor,
        'projetos': projetos,
        'soft_skills': soft_skills,
        'hard_skills': hard_skills,
        'contatos': contatos,
    })
