# Generated by Django 5.1 on 2024-08-23 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_editora_cidade_editora_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="autor",
            new_name="autores",
        ),
    ]
