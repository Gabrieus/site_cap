# Generated by Django 4.0.2 on 2022-03-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0029_delete_fotospage_fotos_legendapage_fotos_tituloone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloOne', models.CharField(default='Atividades Escolares e', max_length=40, verbose_name='Título I:')),
                ('tituloTwo', models.CharField(default='Eventos', max_length=40, verbose_name='Título II:')),
                ('legenda', models.CharField(blank=True, default='Aqui são postadas as fotos dos nossos eventos e atividades escolares.', max_length=200, null=True, verbose_name='Legenda:')),
            ],
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='legendaPage',
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='tituloOne',
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='tituloTwo',
        ),
    ]
