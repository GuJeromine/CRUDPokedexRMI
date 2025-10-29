# Pokédex CRUD com Pyro5 (Python Remote Objects)

Este projeto implementa um sistema CRUD (Create, Read, Update, Delete) completo para uma Pokédex, utilizando uma arquitetura de cliente-servidor baseada em **Pyro5 (Python Remote Objects)**.

O sistema é composto por quatro componentes principais:
1.  **`banco.py`**: A camada de persistência de dados (Model).
2.  **`pokemon.py`**: A definição do objeto de dados (DTO) e sua lógica de serialização.
3.  **`servidor.py`**: O servidor Pyro que expõe a lógica de negócios (Controller).
4.  **`cliente.py`**: O cliente de console (CLI) que interage com o usuário (View).

## Arquitetura do Projeto

### `banco.py` (Camada de Dados)
* **Tecnologia:** `sqlite3`
* **Responsabilidade:** Gerencia a conexão e a execução de comandos SQL no banco de dados `pokedex.db`.
* **Tabela:** Cria a tabela `pokedex(id, nome, tipo, genero, altura, peso)`.
* **Métodos:** Fornece as funções de banco de dados fundamentais: `adicionar`, `buscar` (por ID), `buscarTudo`, `remover` e `atualizar`.

### `pokemon.py` (Objeto de Dados)
* **Responsabilidade:** Define a classe `Pokemon`, que atua como um Objeto de Transferência de Dados (DTO). Este é o objeto que é passado entre o cliente e o servidor.
* **Serialização Pyro:** Contém as funções `converterPokemonDicionario` (serializador) e `converterDicionario` (desserializador). Elas são essenciais para que o Pyro5 saiba como converter o objeto `Pokemon` em um dicionário (para envio pela rede) e como converter o dicionário de volta em um objeto.

### `servidor.py` (Servidor Pyro)
* **Tecnologia:** `Pyro5.server`
* **Responsabilidade:** Atua como o "controlador" da aplicação.
* **Exposição:** Expõe a classe `CRUD` para ser acessível remotamente. Esta classe encapsula a lógica de negócios, recebendo os dados do cliente e chamando os métodos apropriados do `banco.py`.
* **Registro:** Registra a si mesmo no **Pyro Name Server** (Servidor de Nomes) com o nome lógico `crud`.
* **Serialização:** Configura o Pyro para usar os conversores definidos em `pokemon.py` para lidar com a troca de objetos `Pokemon`.

### `cliente.py` (Cliente CLI)
* **Tecnologia:** `Pyro5.client`
* **Responsabilidade:** Fornece a interface de usuário (View) através de um menu de console.
* **Conexão:** Conecta-se ao **Pyro Name Server** para localizar o objeto remoto registrado como `crud` e cria um *proxy* para ele.
* **Operações:** Apresenta um menu (1 a 6) que permite ao usuário:
    1.  **Inserir:** Coleta os dados, cria um objeto `Pokemon` e o envia ao servidor.
    2.  **Buscar (por ID):** Envia um ID e imprime o resultado.
    3.  **Atualizar:** Coleta um ID e os novos dados para atualizar um registro.
    4.  **Remover:** Envia um ID para remoção.
    5.  **Buscar Tudo:** Solicita e imprime todos os Pokémon do banco.
* **Validação:** Inclui validação de entrada do usuário para garantir que os tipos de dados (texto, números) estejam corretos antes de enviá-los ao servidor.

## Como Executar

Para rodar este projeto, você precisa executar três componentes em terminais separados, na seguinte ordem:

1.  **Iniciar o Pyro Name Server:**
    Use um dos comandos a seguir no seu terminal:
    ```bash
    python -m Pyro5.nameserver
    ```
    *(Ou, se estiver no seu PATH, o atalho):*
    ```bash
    pyro5-ns
    ```

2.  **Iniciar o Servidor:**
    (Em um novo terminal)
    ```bash
    python servidor.py
    ```
    *Você verá uma saída indicando a URI do servidor e que ele está pronto.*

3.  **Iniciar o Cliente:**
    (Em um novo terminal)
    ```bash
    python cliente.py
    ```
