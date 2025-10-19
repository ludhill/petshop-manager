from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TipoAnimal, Raca, Animal
from django.shortcuts import render
from django.contrib import messages

class AnimalCreateView(CreateView):
    model = Animal
    # Os campos 'tipo_animal' e 'raca' serão renderizados manualmente no template
    # Adicione 'sexo' à lista de campos
    fields = ['nome', 'data_nascimento', 'sexo', 'tipo_animal', 'raca']
    template_name = 'management/animal_form.html'
    # ATENÇÃO: Crie uma URL chamada 'home' ou mude para uma que já exista
    success_url = reverse_lazy('home')

    # Esta função adiciona dados extras ao contexto do template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicionamos a lista de tipos de animais ativos para popular o primeiro select
        context['tipos_de_animais'] = TipoAnimal.objects.filter(ativo=True)
        return context
    
    # Esta função associa o animal ao usuário logado (requer login)
    def form_valid(self, form):
        form.instance.proprietario = self.request.user
        messages.success(self.request, f"O animal '{form.instance.nome}' foi cadastrado com sucesso!")
        return super().form_valid(form)
        
# --- Views para TipoAnimal ---
class TipoAnimalListView(ListView):
    model = TipoAnimal
    template_name = 'management/tipoanimal_list.html' # template que vamos criar

class TipoAnimalCreateView(CreateView):
    model = TipoAnimal
    fields = ['nome', 'icone']
    template_name = 'management/tipoanimal_form.html' # template que vamos criar
    success_url = reverse_lazy('tipoanimal_list') # Redireciona para a lista após criar

# --- Views para Raca ---
class RacaListView(ListView):
    model = Raca
    template_name = 'management/raca_list.html'

class RacaCreateView(CreateView):
    model = Raca
    fields = ['tipo_animal', 'nome', 'observacoes_manejo']
    template_name = 'management/raca_form.html'
    success_url = reverse_lazy('raca_list')

# --- API para buscar raças dinamicamente ---
def get_racas_by_tipo(request):
    tipo_animal_id = request.GET.get('tipo_id')
    # Filtramos apenas as raças ativas
    racas = Raca.objects.filter(tipo_animal_id=tipo_animal_id, ativo=True).order_by('nome')
    # Convertemos o queryset para uma lista de dicionários para o JSON
    return JsonResponse(list(racas.values('id', 'nome')), safe=False)
    
def home(request):
    # 2. BUSQUE OS ANIMAIS NO BANCO DE DADOS
    # Vamos pegar apenas os ativos e ordenar por nome
    animais_cadastrados = Animal.objects.filter(ativo=True).order_by('nome')

    # 3. PASSE OS DADOS PARA O TEMPLATE ATRAVÉS DO CONTEXTO
    context = {
        'animais': animais_cadastrados
    }
    return render(request, 'management/home.html', context)