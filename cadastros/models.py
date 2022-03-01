import django.utils.timezone
from django.db import models


class Noticias(models.Model):
    titulo = models.CharField('Título:', max_length=50)
    imagem = models.ImageField('Imagem:', default='slides/slide_padrao.png', upload_to='slides')
    legenda = models.CharField('Legenda:', max_length=100)
    texto = models.TextField('Texto:')
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
    legenda = models.CharField('Legenda:', max_length=100)
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
    legenda = models.TextField('Legenda:', default='Aqui disponibilizamos várias formas para nos encontrar', null=True, blank=True)
    enderecoCap = models.TextField('Endereço CAP:', default='Endereço: Av. Getúlio Vargas, 654 - Centro, Rio Branco - AC, 69900-150', null=True, blank=True)
    emailCap = models.EmailField('Email CAP:', default='cap@ufac.br', null=True, blank=True)
    foneCap = models.CharField('Telefone CAP:', max_length=20, default='(68) 99971-3692', null=True, blank=True)

    def __str__(self):
        return self.titulo
