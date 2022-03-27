import datetime

import django.utils.timezone
from django.db import models
from ckeditor.fields import RichTextField


class Noticias(models.Model):
    titulo = models.CharField('Título:', max_length=100)
    imagem = models.ImageField('Imagem:', default='slides/slide_padrao.png', upload_to='slides')
    # legenda = models.CharField('Legenda:', max_length=100, null=True, blank=True, default='')
    # texto = models.TextField('Texto:')
    texto = RichTextField('Texto:')
    autor = models.CharField('Autor:', max_length=100, default='Equipe Gestora', null=True, blank=True)
    data = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.titulo


class Fotos(models.Model):
    ESCOLHAS = (
        ("FUND_I", "Fundamental I"),
        ("FUND_II", "Fundamental II"),
        ("MEDIO", "Médio"),
    )

    titulo = models.CharField('Título:', max_length=50)
    imagem = models.ImageField('Imagem:', default='fotos/foto_padrao.png', upload_to='fotos')
    legenda = models.CharField('Legenda:', max_length=100, null=True, blank=True, default=datetime.date.today().year)
    categoria = models.CharField('Categoria:', choices=ESCOLHAS, max_length=20, default='FUND_I')
    data = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.titulo


class ContatoForm(models.Model):
    nome = models.CharField('Nome:', max_length=100)
    email = models.EmailField('E-mail:')
    assunto = models.CharField('Assunto:', max_length=100)
    mensagem = models.TextField('Mensagem:')
    data = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.nome


class ContatoPage(models.Model):
    titulo = models.CharField('Título:', max_length=40, default='Nossos Contatos')
    legenda = models.CharField('Legenda:', max_length=200,
                               default='Aqui disponibilizamos várias formas para nos encontrar', null=True, blank=True)
    enderecoCap = models.TextField('Endereço CAP:',
                                   default='Endereço: Av. Getúlio Vargas, 654 - Centro, Rio Branco - AC, 69900-150',
                                   null=True, blank=True)
    emailCap = models.EmailField('Email CAP:', default='cap@ufac.br', null=True, blank=True)
    foneCap = models.CharField('Telefone CAP:', max_length=20, default='(68) 99971-3692', null=True, blank=True)
    mapaCap = models.TextField('Link do Mapa: ',
                              default='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15718.196648683606!2d-67.8106109!3d-9.9714163!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x589d3c359dec27ca!2zQ29sw6lnaW8gZGUgQXBsaWNhw6fDo28gZGEgVWZhYw!5e0!3m2!1spt-BR!2sbr!4v1644278509347!5m2!1spt-BR!2sbr',
                              max_length=400)

    def __str__(self):
        return self.titulo


class FotosPage(models.Model):
    titulo_one = models.CharField('Título I:', max_length=100, default='Atividades Escolares e')
    titulo_two = models.CharField('Título II:', max_length=100, default='Eventos')
    legenda = models.CharField('Legenda:', max_length=200,
                               default='Aqui são postadas as fotos dos nossos eventos e atividades escolares',
                               null=True, blank=True)

    def __str__(self):
        return self.titulo_one


class Pilares(models.Model):
    titulo_one = models.CharField('Título I:', max_length=100, blank=True, null=True, default='MISSÃO')
    pilar_one = models.TextField('Pilar I:', blank=True, null=True)
    titulo_two = models.CharField('Título II:', max_length=100, blank=True, null=True, default='VISÃO')
    pilar_two = models.TextField('Pilar II:', blank=True, null=True)
    titulo_three = models.CharField('Título III:', max_length=100, blank=True, null=True, default='VALORES')
    pilar_three = models.TextField('Pilar III:', blank=True, null=True)

    def __str__(self):
        return self.titulo_one


class GestaoHeader(models.Model):
    titulo_one = models.CharField('Título I:', max_length=100, default='Nossa')
    titulo_two = models.CharField('Título II:', max_length=100, default='Gestão')
    legenda = models.CharField('Legenda:', max_length=300,
                               default='É com alegria que iniciamos o ano letivo de 2022 e o segundo ano da nossa gestão que tem como lema "Com União Podemos Mais".',
                               null=True, blank=True)

    def __str__(self):
        return self.titulo_one


class GestaoPage(models.Model):
    nome = models.CharField('Nome:', max_length=100)
    cargo = models.CharField('Cargo:', max_length=200)
    twitter = models.URLField('Twitter:', default='https://www.twitter.com')
    face = models.URLField('Facebook:', default='https://www.facebook.com')
    insta = models.URLField('Instagram:', default='https://www.instagram.com')
    linkedin = models.URLField('Linkedin:', default='https://www.linkedin.com')
    imagem = models.ImageField('Foto:', upload_to='gestores')

    def __str__(self):
        return self.nome


class ServicosPage(models.Model):
    titulo_one = models.CharField('Título I:', max_length=100, default='Alguns dos nossos')
    titulo_two = models.CharField('Título II:', max_length=100, default='Serviços')
    legenda = models.CharField('Legenda:', max_length=300,
                               default='Relação de alguns dos nossos serviços que você aluno(a) pode solicitar online.',
                               null=True, blank=True)

    def __str__(self):
        return self.titulo_one


class Servicos(models.Model):
    servico = models.CharField('Serviço:', max_length=100)
    descricao = models.TextField('Descrição:')
    icone = models.CharField('Ícone:', max_length=300, default='<i class="bx bx-file"></i>')
    link = models.URLField('URL:', default='')

    def __str__(self):
        return self.servico


class SobreHeader(models.Model):
    titulo_one = models.CharField('Título I:', max_length=100, default='Saiba mais sobre')
    titulo_two = models.CharField('Título II:', max_length=100, default='nosso colégio')
    legenda = models.CharField('Legenda:', max_length=300,
                               default='Aqui vamos começar a contar um pouco sobre os nossos 41 anos!',
                               null=True, blank=True)

    def __str__(self):
        return self.titulo_one


class SobrePage(models.Model):
    titulo = models.CharField('Título:', max_length=100)
    subtitulo = models.CharField('Subtítulo:', max_length=300)
    texto = models.TextField('Texto:')
    imagem = models.ImageField('Imagem:', default='pages/sobre_default.jpg', upload_to='pages')
