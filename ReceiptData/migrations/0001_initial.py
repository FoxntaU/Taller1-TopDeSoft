# Generated by Django 4.2.4 on 2024-03-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos/')),
            ],
        ),
        migrations.CreateModel(
            name='Datosnoestructurados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('archivos', models.ManyToManyField(to='ReceiptData.archivo')),
            ],
        ),
    ]