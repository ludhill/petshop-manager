# Petshop Manager - Sistema de Gestão para Petshops

Este é o repositório do projeto **Petshop Manager**, um sistema web desenvolvido em Django para a gestão completa das operações de um petshop ou clínica veterinária. O foco inicial deste desenvolvimento foi a criação de um módulo robusto para o gerenciamento de animais, seus tipos e raças, com uma base sólida para futuras expansões.

## Lógica e Funcionalidades Desenvolvidas

O núcleo do sistema implementado até o momento concentra-se na gestão de cadastros essenciais para o funcionamento do petshop.

1.  **Módulo de Gestão (`management`):**

      * [cite\_start]**Tipos de Animais:** Permite o cadastro de espécies (ex: Cachorro, Gato), utilizando um seletor de ícones da biblioteca Font Awesome para uma interface mais visual e amigável, em vez de um sistema de upload de imagens[cite: 32].
      * **Raças:** Cadastro de raças, sempre associadas a um "Tipo de Animal" previamente cadastrado. [cite\_start]Isso garante a consistência e a organização dos dados[cite: 42].
      * **Animais:** Cadastro completo de animais, vinculando-os a um tutor (atualmente um usuário do sistema), tipo, raça, e incluindo informações como nome, data de nascimento e sexo.

2.  **Interface Dinâmica:**

      * O formulário de cadastro de animais possui um sistema dinâmico onde a seleção do "Tipo de Animal" filtra automaticamente as raças correspondentes, consumindo uma API interna. [cite\_start]Isso evita erros de cadastro, como associar uma raça de gato a um cachorro[cite: 43].

3.  **Feedback ao Usuário:**

      * O sistema utiliza o *Django Messages Framework* para fornecer feedback claro ao usuário após ações importantes, como o cadastro bem-sucedido de um animal.

4.  **Estrutura de Layout:**

      * Foi implementado um template base (`base.html`) com uma barra de navegação (Navbar) que é herdada por todas as outras páginas, garantindo uma experiência de usuário consistente e facilitando a manutenção do layout.

## Estrutura de Pastas e Ficheiros

A organização do projeto segue as melhores práticas do Django, separando o projeto principal das suas aplicações.

  * `projeto_petshop/` (Raiz)
      * **`manage.py`**: O script principal para interagir com o projeto via linha de comando (rodar o servidor, criar migrações, etc.).
      * **`templates/`**: Contém os templates globais compartilhados por toda a aplicação.
          * **`base.html`**: O layout principal com a navbar, que todas as outras páginas herdam.
          * **`404.html` / `500.html`**: Páginas de erro personalizadas para uma experiência de usuário mais profissional.
      * **`petshop_project/`**: A pasta de configuração do projeto.
          * **`settings.py`**: O coração do projeto. Define o banco de dados, os apps instalados, a localização dos templates, etc.
          * **`urls.py`**: O arquivo de rotas principal, que direciona as URLs para os respectivos apps.
      * **`management/`**: O nosso app, responsável por toda a lógica de cadastros.
          * **`models.py`**: Define a estrutura das tabelas do banco de dados (as classes `TipoAnimal`, `Raca`, `Animal`).
          * **`views.py`**: Contém a lógica de back-end. É aqui que o sistema busca dados no banco e os envia para os templates.
          * **`urls.py`**: Define as rotas específicas deste app (ex: `/management/animal/novo/`).
          * **`admin.py`**: Configura como os modelos aparecerão na interface de administração do Django.
          * **`migrations/`**: Armazena o histórico de alterações feitas no banco de dados.
          * **`templates/management/`**: Contém os templates específicos deste app (`animal_form.html`, `home.html`, etc.), seguindo a prática de *namespacing*.

## Comandos Importantes

Para o bom funcionamento e depuração do sistema, utilize os seguintes comandos no terminal, sempre com o ambiente virtual (`venv`) ativado.

  * **Ativar Ambiente Virtual (Windows):**

    ```bash
    .\venv\Scripts\activate
    ```

  * **Instalar Dependências:**

    ```bash
    pip install -r requirements.txt 
    ```

    *(Nota: Crie um arquivo `requirements.txt` com `pip freeze > requirements.txt` para listar as dependências como Django, Pillow, etc.)*

  * **Criar/Aplicar Alterações no Banco de Dados:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

  * **Rodar o Servidor de Desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

  * **Criar um Superusuário (para acesso ao Admin):**

    ```bash
    python manage.py createsuperuser
    ```

  * **Acessar o Shell Interativo (para depuração):**

    ```bash
    python manage.py shell
    ```

## Ambientes de Usuário

No estágio atual, o sistema opera principalmente com um ambiente de administração centralizado.

  * **Ambiente Admin (`/admin`):**

      * Este é o painel de controle principal, acessível pelo superusuário.
      * É utilizado para a gestão completa dos dados: criar, visualizar, editar e deletar Tipos, Raças e Animais.
      * Funciona como a principal ferramenta para o "Gestor" do sistema no momento.

  * **Demais Usuários (Ambiente Front-end):**

      * O front-end permite a visualização (na home) e o cadastro de novos animais.
      * **Importante:** Atualmente, a funcionalidade de cadastro de animais exige que o usuário **esteja logado no sistema** (pode ser com a mesma conta do superusuário). Sem login, o cadastro falhará silenciosamente.

    *A gestão granular de papéis e permissões (Tutor, Colaborador, Gestor) não foi o foco desta fase do projeto, sendo uma das principais melhorias futuras.*

## Limitações de Usabilidade e Sugestões de Melhoria

O sistema é funcional, mas possui limitações importantes a serem consideradas para a evolução do projeto.

  * **Limitações Atuais:**

    1.  **Tutor = Usuário:** A maior limitação é que todo tutor de um animal precisa, obrigatoriamente, ter uma conta de usuário com login e senha no sistema. Isso é inviável para clientes que não têm familiaridade com tecnologia.
    2.  **Falta de Permissões Granulares:** Não há distinção entre o que um "Gestor" e um "Colaborador" podem ver ou fazer no front-end. Todas as funcionalidades são abertas para qualquer usuário logado.
    3.  **Gestão de "Ativo":** A opção de marcar um animal como "Ativo" ou "Inativo" só está disponível na interface de Admin, não sendo acessível por um "Gestor" no ambiente principal do sistema.

  * **Sugestões de Melhorias Futuras:**

    1.  **Criar o Modelo `Tutor`:** Desacoplar os dados do cliente (Nome, CPF, Telefone) da conta de acesso (`Usuário`). Isso permitiria o cadastro de tutores no balcão sem a necessidade de criar um login para eles.
    2.  **Implementar Papéis e Permissões:** Desenvolver um sistema que restrinja o acesso a funcionalidades com base no papel do usuário (Tutor, Colaborador, Gestor), conforme discutido.
    3.  **Dashboard do Tutor:** Criar uma área logada para o cliente (Tutor), onde ele possa ver apenas os seus animais e seu histórico.
    4.  **Melhorar a Interface de Gestão:** Trazer funcionalidades do Admin (como a gestão do status "Ativo") para a interface principal, tornando-a acessível para o perfil de "Gestor".

## Observações Adicionais

  * O projeto está configurado para usar um banco de dados **PostgreSQL** hospedado na plataforma **Supabase**, garantindo um ambiente de desenvolvimento robusto e escalável. As credenciais de acesso são gerenciadas de forma segura através de um arquivo `.env`.
  * O termo "Proprietário" foi utilizado inicialmente, mas a sugestão é refatorar o código futuramente para usar o termo **"Tutor"**, que é mais adequado ao contexto de petshops.
