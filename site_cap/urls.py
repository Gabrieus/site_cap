from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="base.html"), name='index'),
    # path('base/', TemplateView.as_view(template_name="base.html"), name='base'),
    # path('servicos/', TemplateView.as_view(template_name="servicos.html"), name='servicos'),
    # path('gestao/', TemplateView.as_view(template_name="gestao.html"), name='gestao'),
    # path('sobre/', TemplateView.as_view(template_name="sobre.html"), name='sobre'),
    path('professores/', TemplateView.as_view(template_name="professores.html"), name='professores'),
    path('alunos/', TemplateView.as_view(template_name="alunos.html"), name='alunos'),
    path('admSite/', TemplateView.as_view(template_name="baseAdm.html"), name='admSite'),
    path('', include('cadastros.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
