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


def teste_htmx(request):
    return render(request, 'portifolio/testes_htmx.html')


def content(request):
    return render(request, 'portifolio/content.html')


def page_1(request):
    pessoas_query = [
        {'nome': 'Werbety', 'sexo': 'M'},
        {'nome': 'Maria', 'sexo': 'F'},
        {'nome': 'Alex', 'sexo': 'M'},
        {'nome': 'Ana', 'sexo': 'F'},
    ]
    return render(request, 'portifolio/page_1.html', context={
        'pessoas': pessoas_query
        })


def page_2(request):
    return render(request, 'portifolio/page_2.html')


def page_3(request):
    return render(request, 'portifolio/page_3.html')
