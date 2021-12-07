# Generated by Django 3.2.9 on 2021-12-07 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('arquivo', models.FileField(upload_to='')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.disciplina')),
            ],
        ),
    ]