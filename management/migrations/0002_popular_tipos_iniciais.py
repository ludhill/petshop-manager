from django.db import migrations
 
TIPOS_INICIAIS = [
    {"nome": "Cachorro", "icone": "fas fa-dog"},
    {"nome": "Gato", "icone": "fas fa-cat"},
    {"nome": "Pássaro", "icone": "fas fa-dove"},
    {"nome": "Peixe", "icone": "fas fa-fish"},
    {"nome": "Roedor", "icone": "fas fa-otter"}, 
]

def popular_dados(apps, schema_editor):
    TipoAnimal = apps.get_model('management', 'TipoAnimal')
    for tipo_data in TIPOS_INICIAIS:
        TipoAnimal.objects.create(nome=tipo_data["nome"], icone=tipo_data["icone"])

def reverter_dados(apps, schema_editor):
    TipoAnimal = apps.get_model('management', 'TipoAnimal')
    for tipo_data in TIPOS_INICIAIS:
        TipoAnimal.objects.filter(nome=tipo_data["nome"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(popular_dados, reverse_code=reverter_dados),
    ]