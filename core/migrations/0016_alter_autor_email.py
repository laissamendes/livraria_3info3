# Generated by Django 5.1 on 2024-08-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_rename_autor_livro_autores"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="email",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]