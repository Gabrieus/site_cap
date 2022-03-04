from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Noticias, Fotos, ContatoForm, ContatoPage, FotosPage
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render


def abertura_modelform(request):
    return render(request, "base.html")


# ================ Notícias ================ #


class NoticiasCad(SuccessMessageMixin, CreateView):
    model = Noticias
    fields = ['titulo', 'imagem', 'legenda', 'texto']
    template_name = 'cadastros/noticiasCreateAndUpdate.html'
    success_url = reverse_lazy('cadNoticias')
    success_message = "Notícia criada com sucesso! Recarregue a lista para ver."


class NoticiasListagem(ListView):
    model = Noticias
    template_name = 'cadastros/noticiasRead.html'


class NoticiasUpdate(UpdateView):
    model = Noticias
    fields = "__all__"
    template_name = 'cadastros/noticiasCreateAndUpdate.html'
    success_url = reverse_lazy('listNoticias')


class NoticiasDelete(DeleteView):
    model = Noticias
    template_name = 'cadastros/noticiasDelete.html'
    success_url = reverse_lazy('listNoticias')

# ================ Fotos ================ #


class FotosCad(SuccessMessageMixin, CreateView):
    model = Fotos
    fields = ['titulo', 'imagem', 'legenda', 'categoria']
    template_name = 'cadastros/fotosCreateAndUpdate.html'
    success_url = reverse_lazy('cadFotos')
    success_message = "Foto publicada com sucesso! Recarregue a lista para ver."


class FotosListagem(ListView):
    model = Fotos
    template_name = 'cadastros/fotosRead.html'


class FotosUpdate(UpdateView):
    model = Fotos
    fields = "__all__"
    template_name = 'cadastros/fotosCreateAndUpdate.html'
    success_url = reverse_lazy('listFotos')


class FotosDelete(DeleteView):
    model = Fotos
    template_name = 'cadastros/fotosDelete.html'
    success_url = reverse_lazy('listFotos')


class FotosPag(ListView):
    model = Fotos
    template_name = 'cadastros/fotos.html'


# ================ Fotos/Eventos Page ================ #

class FotosPageCreate(SuccessMessageMixin, CreateView):
    model = FotosPage
    fields = ['tituloOne', 'tituloTwo', 'legenda']
    template_name = 'cadastros/fotosPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageFotos')
    success_message = "A página fotos foi atualizada com sucesso!"


class FotosPageUpdate(UpdateView):
    model = FotosPage
    fields = ['tituloOne', 'tituloTwo', 'legenda']
    template_name = 'cadastros/fotosPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageFotos')


class FotosPageList(ListView):
    model = FotosPage
    template_name = 'cadastros/fotosPage_Read.html'


class FotosPageDelete(DeleteView):
    model = FotosPage
    template_name = 'cadastros/fotosPage_Delete.html'
    success_url = reverse_lazy('listPageFotos')


class FotosPageView(ListView):
    model = FotosPage
    template_name = 'cadastros/fotos.html'

# ================ Contato Page ================ #


class ContatoPageCreate(SuccessMessageMixin, CreateView):
    model = ContatoPage
    fields = ['titulo', 'legenda', 'emailCap', 'foneCap', 'enderecoCap', 'mapaCap']
    template_name = 'cadastros/contatoPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageContato')
    success_message = "A página contato foi atualizada com sucesso!"


class ContatoPageUpdate(UpdateView):
    model = ContatoPage
    fields = ['titulo', 'legenda', 'emailCap', 'foneCap', 'enderecoCap', 'mapaCap']
    template_name = 'cadastros/contatoPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageContato')


class ContatoPageList(ListView):
    model = ContatoPage
    template_name = 'cadastros/contatoPage_Read.html'


class ContatoPageDelete(DeleteView):
    model = ContatoPage
    template_name = 'cadastros/contatoPage_Delete.html'
    success_url = reverse_lazy('listPageContato')


class ContatoPageView(ListView):
    model = ContatoPage
    template_name = 'contato.html'


# ================ Contato Form ================ #

class ContatoCad(SuccessMessageMixin, CreateView):
    model = ContatoForm
    fields = ['nome', 'email', 'assunto', 'mensagem']
    template_name = 'cadastros/contatoForm_CreateAndUpdate.html'
    success_url = reverse_lazy('cadContato')
    success_message = "Sua mensagem foi enviada com sucesso!"


class ContatoList(ListView):
    model = ContatoForm
    template_name = 'cadastros/contatoForm_Read.html'


class ContatoDelete(DeleteView):
    model = ContatoForm
    template_name = 'cadastros/contatoForm_Delete.html'
    success_url = reverse_lazy('listContato')


