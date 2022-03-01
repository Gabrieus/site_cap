from django.urls import path
from cadastros import views
from cadastros.views import NoticiasCad, NoticiasDelete, NoticiasUpdate, NoticiasListagem
from cadastros.views import FotosCad, FotosDelete, FotosUpdate, FotosListagem, FotosPag
from cadastros.views import ContatoCad, ContatoDelete, ContatoList, ContatoPageList
from cadastros.views import ContatoPageDelete, ContatoPageView, ContatoPageUpdate, ContatoPageCreate

urlpatterns = [

    # Urls notícias
    path('cadNoticias/', NoticiasCad.as_view(), name='cadNoticias'),
    path('listNoticias/', NoticiasListagem.as_view(), name='listNoticias'),
    path('editNoticias/<int:pk>', NoticiasUpdate.as_view(), name='editNoticias'),
    path('delNoticias/<int:pk>', NoticiasDelete.as_view(), name='delNoticias'),
    path('', views.abertura_modelform, name='index'),

    # Urls fotos
    path('cadFotos/', FotosCad.as_view(), name='cadFotos'),
    path('listFotos/', FotosListagem.as_view(), name='listFotos'),
    path('editFotos/<int:pk>', FotosUpdate.as_view(), name='editFotos'),
    path('delFotos/<int:pk>', FotosDelete.as_view(), name='delFotos'),
    path('fotos/', FotosPag.as_view(), name='fotos'),

    # = Urls Contato = #

    # == Form == #
    path('cadContato/', ContatoCad.as_view(), name='cadContato'),
    path('listContato/', ContatoList.as_view(), name='listContato'),
    path('delContato/<int:pk>', ContatoDelete.as_view(), name='delContato'),
    # == Page == #
    path('cadPageContato/', ContatoPageCreate.as_view(), name='cadPageContato'),
    path('listPageContato/', ContatoPageList.as_view(), name='listPageContato'),
    path('editPageContato/<int:pk>', ContatoPageUpdate.as_view(), name='editPageContato'),
    path('delPageContato/<int:pk>', ContatoPageDelete.as_view(), name='delPageContato'),
    path('contato/', ContatoPageView.as_view(), name='contato'),
]
