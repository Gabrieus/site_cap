from django.urls import path
from cadastros import views
from cadastros.views import ServicosCreate, ServicosUpdate, ServicosList, ServicosDelete, ServicosPage
from cadastros.views import NoticiasCad, NoticiasDelete, NoticiasUpdate, NoticiasListagem, NoticiasPageList, NoticiasArticleView
from cadastros.views import PilaresPageView, PilaresPageCreate, PilaresPageUpdate, PilaresPageDelete, PilaresPageList
from cadastros.views import FotosCad, FotosDelete, FotosUpdate, FotosListagem, FotosPag
from cadastros.views import ContatoCad, ContatoDelete, ContatoList, ContatoPageList
from cadastros.views import ContatoPageDelete, ContatoPageView, ContatoPageUpdate, ContatoPageCreate
from cadastros.views import FotosPageCreate, FotosPageList, FotosPageUpdate, FotosPageDelete, FotosPageView
from cadastros.views import GestaoPageDelete, GestaoPageView, GestaoPageUpdate, GestaoPageCreate, GestaoPageList
from cadastros.views import ServicosPageCreate, ServicosPageList, ServicosPageUpdate, ServicosPageDelete, ServicosPageView
from cadastros.views import GestaoHeaderCreate, GestaoHeaderUpdate, GestaoHeaderList, GestaoHeaderDelete, GestaoHeaderView
from cadastros.views import SobreHeaderCreate, SobreHeaderUpdate, SobreHeaderList, SobreHeaderDelete, SobreHeaderView
from cadastros.views import SobrePageCreate, SobrePageUpdate, SobrePageList, SobrePageDelete, SobrePageView

urlpatterns = [
    path('index/', views.abertura_modelform, name='index'),

    # = Urls notícias = #
    path('cadNoticias/', NoticiasCad.as_view(), name='cadNoticias'),
    path('listNoticias/', NoticiasListagem.as_view(), name='listNoticias'),
    path('editNoticias/<int:pk>', NoticiasUpdate.as_view(), name='editNoticias'),
    path('delNoticias/<int:pk>', NoticiasDelete.as_view(), name='delNoticias'),
    path('inicio/', NoticiasPageList.as_view(), name='inicio'),
    path('noticia/<int:pk>', views.NoticiasArticleView.as_view(), name='noticia'),
    # == Pilares == #
    path('cadPagePilares/', PilaresPageCreate.as_view(), name='cadPagePilares'),
    path('listPagePilares/', PilaresPageList.as_view(), name='listPagePilares'),
    path('editPagePilares/<int:pk>', PilaresPageUpdate.as_view(), name='editPagePilares'),
    path('delPagePilares/<int:pk>', PilaresPageDelete.as_view(), name='delPagePilares'),
    path('', PilaresPageView.as_view(), name='base'),

    # = Urls Fotos/Eventos = #

    # == Cadastro de Fotos == #
    path('cadFotos/', FotosCad.as_view(), name='cadFotos'),
    path('listFotos/', FotosListagem.as_view(), name='listFotos'),
    path('editFotos/<int:pk>', FotosUpdate.as_view(), name='editFotos'),
    path('delFotos/<int:pk>', FotosDelete.as_view(), name='delFotos'),
    # == Fotos/Eventos Page == #
    path('cadPageFotos/', FotosPageCreate.as_view(), name='cadPageFotos'),
    path('listPageFotos/', FotosPageList.as_view(), name='listPageFotos'),
    path('editPageFotos/<int:pk>', FotosPageUpdate.as_view(), name='editPageFotos'),
    path('delPageFotos/<int:pk>', FotosPageDelete.as_view(), name='delPageFotos'),
    path('fotos/', FotosPag.as_view(), name='fotos'),
    path('fotosHeader/', FotosPageView.as_view(), name='fotosHeader'),

    # = Urls Contato = #

    # == Contato Form == #
    path('cadContato/', ContatoCad.as_view(), name='cadContato'),
    path('listContato/', ContatoList.as_view(), name='listContato'),
    path('delContato/<int:pk>', ContatoDelete.as_view(), name='delContato'),
    # == Contato Page == #
    path('cadPageContato/', ContatoPageCreate.as_view(), name='cadPageContato'),
    path('listPageContato/', ContatoPageList.as_view(), name='listPageContato'),
    path('editPageContato/<int:pk>', ContatoPageUpdate.as_view(), name='editPageContato'),
    path('delPageContato/<int:pk>', ContatoPageDelete.as_view(), name='delPageContato'),
    path('contato/', ContatoPageView.as_view(), name='contato'),

    # Urls Sobre
    path('cadSobrePage/', SobrePageCreate.as_view(), name='cadSobrePage'),
    path('listSobrePage/', SobrePageList.as_view(), name='listSobrePage'),
    path('editSobrePage/<int:pk>', SobrePageUpdate.as_view(), name='editSobrePage'),
    path('delSobrePage/<int:pk>', SobrePageDelete.as_view(), name='delSobrePage'),
    path('sobre/', SobrePageView.as_view(), name='sobre'),
    # == Sobre Header == #
    path('cadSobreHeader/', SobreHeaderCreate.as_view(), name='cadSobreHeader'),
    path('listSobreHeader/', SobreHeaderList.as_view(), name='listSobreHeader'),
    path('editSobreHeader/<int:pk>', SobreHeaderUpdate.as_view(), name='editSobreHeader'),
    path('delSobreHeader/<int:pk>', SobreHeaderDelete.as_view(), name='delSobreHeader'),
    path('sobreHeader/', SobreHeaderView.as_view(), name='sobreHeader'),

    # Urls Gestão
    path('cadPageGestao/', GestaoPageCreate.as_view(), name='cadPageGestao'),
    path('listPageGestao/', GestaoPageList.as_view(), name='listPageGestao'),
    path('editPageGestao/<int:pk>', GestaoPageUpdate.as_view(), name='editPageGestao'),
    path('delPageGestao/<int:pk>', GestaoPageDelete.as_view(), name='delPageGestao'),
    path('gestao/', GestaoPageView.as_view(), name='gestao'),
    # == Gestão Header == #
    path('cadGestaoHeader/', GestaoHeaderCreate.as_view(), name='cadGestaoHeader'),
    path('listGestaoHeader/', GestaoHeaderList.as_view(), name='listGestaoHeader'),
    path('editGestaoHeader/<int:pk>', GestaoHeaderUpdate.as_view(), name='editGestaoHeader'),
    path('delGestaoHeader/<int:pk>', GestaoHeaderDelete.as_view(), name='delGestaoHeader'),
    path('gestaoHeader/', GestaoHeaderView.as_view(), name='gestaoHeader'),

    # = Urls Serviços = #

    # == Cadastro de Serviços == #
    path('cadServicos/', ServicosCreate.as_view(), name='cadServicos'),
    path('listServicos/', ServicosList.as_view(), name='listServicos'),
    path('editServicos/<int:pk>', ServicosUpdate.as_view(), name='editServicos'),
    path('delServicos/<int:pk>', ServicosDelete.as_view(), name='delServicos'),
    # == Serviços Page == #
    path('cadPageServicos/', ServicosPageCreate.as_view(), name='cadPageServicos'),
    path('listPageServicos/', ServicosPageList.as_view(), name='listPageServicos'),
    path('editPageServicos/<int:pk>', ServicosPageUpdate.as_view(), name='editPageServicos'),
    path('delPageServicos/<int:pk>', ServicosPageDelete.as_view(), name='delPageServicos'),
    path('servicos/', ServicosPage.as_view(), name='servicos'),
    path('servicosHeader/', ServicosPageView.as_view(), name='servicosHeader'),
]
