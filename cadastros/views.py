from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Noticias, Fotos, Contato
from django.urls import reverse_lazy


def abertura_modelform(request):
    return render(request, "index.html")

# Notícias


class NoticiasCad(CreateView):
    model = Noticias
    fields = ['titulo', 'imagem', 'legenda', 'texto']
    template_name = 'cadastros/adm_noticias.html'
    success_url = reverse_lazy('cadNoticias')


class NoticiasListagem(ListView):
    model = Noticias
    template_name = 'cadastros/listar_noticias.html'


class NoticiasUpdate(UpdateView):
    model = Noticias
    fields = "__all__"
    template_name = 'cadastros/adm_noticias.html'
    success_url = reverse_lazy('listNoticias')


class NoticiasDelete(DeleteView):
    model = Noticias
    template_name = 'cadastros/excluir_noticias.html'
    success_url = reverse_lazy('listNoticias')

# Fotos


class FotosCad(CreateView):
    model = Fotos
    fields = ['titulo', 'imagem', 'legenda', 'categoria']
    template_name = 'cadastros/adm_fotos.html'
    success_url = reverse_lazy('cadFotos')


class FotosListagem(ListView):
    model = Fotos
    template_name = 'cadastros/listar_fotos.html'


class FotosUpdate(UpdateView):
    model = Fotos
    fields = "__all__"
    template_name = 'cadastros/adm_fotos.html'
    success_url = reverse_lazy('listFotos')


class FotosDelete(DeleteView):
    model = Fotos
    template_name = 'cadastros/excluir_fotos.html'
    success_url = reverse_lazy('listFotos')


class FotosPag(ListView):
    model = Fotos
    template_name = 'cadastros/fotos.html'

# Contato


class ContatoCad(CreateView):
    model = Contato
    fields = ['nome', 'email', 'assunto', 'mensagem']
    template_name = 'cadastros/form_contato.html'
    success_url = reverse_lazy('contato_conf')


class ContatoListagem(ListView):
    model = Contato
    template_name = 'cadastros/contato_lista.html'


class ContatoDelete(DeleteView):
    model = Contato
    template_name = 'cadastros/contato_excluir.html'
    success_url = reverse_lazy('contato_lista')
