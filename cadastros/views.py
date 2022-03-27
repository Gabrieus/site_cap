from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Noticias, Fotos, ContatoForm, ContatoPage, FotosPage, Pilares, GestaoPage, ServicosPage, \
    Servicos, GestaoHeader, SobreHeader, SobrePage
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render


def abertura_modelform(request):
    return render(request, "base.html")


# ================ Notícias ================ #


class NoticiasCad(SuccessMessageMixin, CreateView):
    model = Noticias
    fields = ['titulo', 'imagem', 'texto', 'autor']
    template_name = 'cadastros/noticiasCreateAndUpdate.html'
    success_url = reverse_lazy('cadNoticias')
    success_message = "Notícia criada com sucesso!"


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


class NoticiasPageList(ListView):
    model = Noticias
    template_name = 'noticiasPainel.html'


class NoticiasArticleView(DeleteView):
    model = Noticias
    template_name = 'noticia.html'


# ================ Fotos ================ #


class FotosCad(SuccessMessageMixin, CreateView):
    model = Fotos
    fields = ['titulo', 'imagem', 'legenda', 'categoria']
    template_name = 'cadastros/fotosCreateAndUpdate.html'
    success_url = reverse_lazy('cadFotos')
    success_message = "Foto publicada com sucesso!"


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
    fields = ['titulo_one', 'titulo_two', 'legenda']
    template_name = 'cadastros/fotosPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageFotos')
    success_message = "A página fotos foi atualizada com sucesso!"


class FotosPageUpdate(UpdateView):
    model = FotosPage
    fields = ['titulo_one', 'titulo_two', 'legenda']
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
    template_name = 'cadastros/fotosPageHeader.html'


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


# ================ Pilares ================ #

class PilaresPageCreate(SuccessMessageMixin, CreateView):
    model = Pilares
    fields = "__all__"
    template_name = 'cadastros/pilaresPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPagePilares')
    success_message = "A página foi atualizada com sucesso!"


class PilaresPageUpdate(UpdateView):
    model = Pilares
    fields = "__all__"
    template_name = 'cadastros/pilaresPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPagePilares')


class PilaresPageList(ListView):
    model = Pilares
    template_name = 'cadastros/pilaresPage_Read.html'


class PilaresPageDelete(DeleteView):
    model = Pilares
    template_name = 'cadastros/pilaresPage_Delete.html'
    success_url = reverse_lazy('listPagePilares')


class PilaresPageView(ListView):
    model = Pilares
    template_name = 'base.html'


# ================ Gestão ================ #

class GestaoPageCreate(SuccessMessageMixin, CreateView):
    model = GestaoPage
    fields = ['nome', 'cargo', 'twitter', 'face', 'insta', 'linkedin', 'imagem']
    template_name = 'cadastros/gestaoPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageGestao')
    success_message = "A página Gestão foi atualizada com sucesso!"


class GestaoPageUpdate(UpdateView):
    model = GestaoPage
    fields = ['nome', 'cargo', 'twitter', 'face', 'insta', 'linkedin', 'imagem']
    template_name = 'cadastros/gestaoPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageGestao')


class GestaoPageList(ListView):
    model = GestaoPage
    template_name = 'cadastros/gestaoPage_Read.html'


class GestaoPageDelete(DeleteView):
    model = GestaoPage
    template_name = 'cadastros/gestaoPage_Delete.html'
    success_url = reverse_lazy('listPageGestao')


class GestaoPageView(ListView):
    model = GestaoPage
    template_name = 'gestao.html'


# ================ Gestão Header ================ #

class GestaoHeaderCreate(SuccessMessageMixin, CreateView):
    model = GestaoHeader
    fields = ['titulo_one', 'titulo_two', 'legenda']
    template_name = 'cadastros/gestaoHeader_CreateAndUpdate.html'
    success_url = reverse_lazy('listGestaoHeader')
    success_message = "A página Gestão foi atualizada com sucesso!"


class GestaoHeaderUpdate(UpdateView):
    model = GestaoHeader
    fields = ['titulo_one', 'titulo_two', 'legenda']
    template_name = 'cadastros/gestaoHeader_CreateAndUpdate.html'
    success_url = reverse_lazy('listGestaoHeader')


class GestaoHeaderList(ListView):
    model = GestaoHeader
    template_name = 'cadastros/gestaoHeader_Read.html'


class GestaoHeaderDelete(DeleteView):
    model = GestaoHeader
    template_name = 'cadastros/gestaoHeader_Delete.html'
    success_url = reverse_lazy('listGestaoHeader')


class GestaoHeaderView(ListView):
    model = GestaoHeader
    template_name = 'cadastros/gestaoHeader.html'


# ================ Serviços Page ================ #

class ServicosPageCreate(SuccessMessageMixin, CreateView):
    model = ServicosPage
    fields = ['titulo_one', 'titulo_two', 'legenda']
    template_name = 'cadastros/servicosPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageServicos')
    success_message = "A página serviços foi atualizada com sucesso!"


class ServicosPageUpdate(UpdateView):
    model = ServicosPage
    fields = ['titulo_one', 'titulo_two', 'legenda']
    template_name = 'cadastros/servicosPage_CreateAndUpdate.html'
    success_url = reverse_lazy('listPageServicos')


class ServicosPageList(ListView):
    model = ServicosPage
    template_name = 'cadastros/servicosPage_Read.html'


class ServicosPageDelete(DeleteView):
    model = ServicosPage
    template_name = 'cadastros/servicosPage_Delete.html'
    success_url = reverse_lazy('listPageServicos')


class ServicosPageView(ListView):
    model = ServicosPage
    template_name = 'cadastros/servicosPageHeader.html'


# ================ Serviços Cards ================ #

class ServicosCreate(SuccessMessageMixin, CreateView):
    model = Servicos
    fields = ['servico', 'descricao', 'icone', 'link']
    template_name = 'cadastros/servicos_CreateAndUpdate.html'
    success_url = reverse_lazy('listServicos')
    success_message = "A página serviços foi atualizada com sucesso!"


class ServicosUpdate(UpdateView):
    model = Servicos
    fields = ['servico', 'descricao', 'icone', 'link']
    template_name = 'cadastros/servicos_CreateAndUpdate.html'
    success_url = reverse_lazy('listServicos')


class ServicosList(ListView):
    model = Servicos
    template_name = 'cadastros/servicos_Read.html'


class ServicosDelete(DeleteView):
    model = Servicos
    template_name = 'cadastros/servicos_Delete.html'
    success_url = reverse_lazy('listServicos')


class ServicosPage(ListView):
    model = Servicos
    template_name = 'servicos.html'


# ================ Sobre Header ================ #

class SobreHeaderCreate(SuccessMessageMixin, CreateView):
    model = SobreHeader
    fields = ['titulo_one', 'titulo_two', 'legenda']
    template_name = 'cadastros/sobreHeader_CreateAndUpdate.html'
    success_url = reverse_lazy('listSobreHeader')
    success_message = "A página Sobre foi atualizada com sucesso!"


class SobreHeaderUpdate(UpdateView):
    model = SobreHeader
    fields = ['titulo_one', 'titulo_two', 'legenda']
    template_name = 'cadastros/sobreHeader_CreateAndUpdate.html'
    success_url = reverse_lazy('listSobreHeader')


class SobreHeaderList(ListView):
    model = SobreHeader
    template_name = 'cadastros/sobreHeader_Read.html'


class SobreHeaderDelete(DeleteView):
    model = SobreHeader
    template_name = 'cadastros/sobreHeader_Delete.html'
    success_url = reverse_lazy('listSobreHeader')


class SobreHeaderView(ListView):
    model = SobreHeader
    template_name = 'cadastros/sobreHeader.html'


# ================ Sobre Page ================ #

class SobrePageCreate(SuccessMessageMixin, CreateView):
    model = SobrePage
    fields = ['titulo', 'subtitulo', 'texto', 'imagem']
    template_name = 'cadastros/sobrePage_CreateAndUpdate.html'
    success_url = reverse_lazy('listSobrePage')
    success_message = "A página Sobre foi atualizada com sucesso!"


class SobrePageUpdate(UpdateView):
    model = SobrePage
    fields = ['titulo', 'subtitulo', 'texto', 'imagem']
    template_name = 'cadastros/sobrePage_CreateAndUpdate.html'
    success_url = reverse_lazy('listSobrePage')


class SobrePageList(ListView):
    model = SobrePage
    template_name = 'cadastros/sobrePage_Read.html'


class SobrePageDelete(DeleteView):
    model = SobrePage
    template_name = 'cadastros/sobrePage_Delete.html'
    success_url = reverse_lazy('listSobrePage')


class SobrePageView(ListView):
    model = SobrePage
    template_name = 'sobre.html'
