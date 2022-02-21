from django.urls import path
from cadastros import views
from cadastros.views import NoticiasCad, NoticiasDelete, NoticiasUpdate, NoticiasListagem
from cadastros.views import FotosCad, FotosDelete, FotosUpdate, FotosListagem, FotosPag
from cadastros.views import ContatoCad, ContatoDelete, ContatoListagem

urlpatterns = [

    # Urls notícias
    path('', views.abertura_modelform, name='index'),
    path('cadNoticias/', NoticiasCad.as_view(), name='cadNoticias'),
    path('listNoticias/', NoticiasListagem.as_view(), name='listNoticias'),
    path('editNoticias/<int:pk>', NoticiasUpdate.as_view(), name='editNoticias'),
    path('delNoticias/<int:pk>', NoticiasDelete.as_view(), name='delNoticias'),

    # Urls fotos
    path('cadFotos/', FotosCad.as_view(), name='cadFotos'),
    path('listFotos/', FotosListagem.as_view(), name='listFotos'),
    path('editFotos/<int:pk>', FotosUpdate.as_view(), name='editFotos'),
    path('delFotos/<int:pk>', FotosDelete.as_view(), name='delFotos'),
    path('fotos/', FotosPag.as_view(), name='fotos'),

    # Urls contato
    path('form_contato/', ContatoCad.as_view(), name='form_contato'),
    path('contato_lista/', ContatoListagem.as_view(), name='contato_lista'),
    path('contato_excluir/<int:pk>', ContatoDelete.as_view(), name='contato_excluir'),

]
