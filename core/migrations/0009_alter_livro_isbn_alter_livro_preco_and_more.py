# Generated by Django 5.0.2 on 2024-08-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_livro_autor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="isbn",
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name="ISBN"),
        ),
        migrations.AlterField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name="Preço"
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="titulo",
            field=models.CharField(max_length=255, verbose_name="Título"),
        ),
    ]
