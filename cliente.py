import Pyro5.client
import sys
import pokemon
import Pyro5.api

CRUD_proxy = Pyro5.client.Proxy('PYRONAME:crud')

if not CRUD_proxy._pyroBind():
    sys.exit(-1)

# pois envia objetos
Pyro5.api.register_class_to_dict(pokemon.Pokemon,
                                 pokemon.converterPokemonDicionario)

opcao = None
while opcao != '6':

    opcao = input('Digite 1 para inserir, 2 para buscar, 3 para atualizar, 4 para remover, 5 para buscar tudo, 6 para sair\n')

    match opcao:
        case '1':
            while True:
                nome = input('digite nome do pokemon: ')
                if nome and not nome.isdigit(): # Verifica se não está vazio e se não é um número
                    break # Se for válido, sai do loop
                print("Erro: Nome inválido. Por favor, digite um texto.")
            while True:
                tipo = input('digite tipo do pokemon: ')
                if tipo and not tipo.isdigit():
                    break
                print("Erro: Tipo inválido. Por favor, digite um texto.")
            while True:
                genero = input('digite genero do pokemon: ')
                if genero and not genero.isdigit():
                    break
                print("Erro: Gênero inválido. Por favor, digite um texto.")
            while True:
                try:
                    altura = float(input('digite a altura do pokémon: '))
                    break # Se for válido, sai do loop
                except ValueError:
                    print("Erro: Altura inválida. Por favor, digite um número.")
            while True:
                try:
                    peso = float(input('digite o peso do pokémon: '))
                    break # Se for válido, sai do loop
                except ValueError:
                    print("Erro: Peso inválido. Por favor, digite um número.")

            d = pokemon.Pokemon(nome,tipo,genero,altura,peso)
            id = CRUD_proxy.adicionar(d)

            if id is not None:
                print('Dado inserido com id', id)
            else:
                print('Dado não foi inserido')
        case '2':
            try:
                id = int(input('digite id do pokemon: '))
                dados = CRUD_proxy.buscar(id)
                if dados is not None:
                    print('Dados encontrados:', dados)
                else:
                    print('Dados não encontrados')
            except ValueError:
                print("Erro: ID inválido. Por favor, digite um número inteiro.")
            
        case '3':
            try:
                    id = int(input('digite id do pokemon: '))
                    if CRUD_proxy.buscar(id) is not None:
                        while True:
                            nome = input('digite novo nome do pokemon: ')
                            if nome and not nome.isdigit(): # Verifica se não está vazio e se não é um número
                                break # Se for válido, sai do loop
                            print("Erro: Nome inválido. Por favor, digite um texto.")
                        while True:
                            tipo = input('digite novo tipo do pokemon: ')
                            if tipo and not tipo.isdigit():
                                break
                            print("Erro: Tipo inválido. Por favor, digite um texto.")
                        while True:
                            genero = input('digite novo genero do pokemon: ')
                            if genero and not genero.isdigit():
                                break
                            print("Erro: Gênero inválido. Por favor, digite um texto.")
                        while True:
                            try:
                                altura = float(input('digite nova altura do pokemon: '))
                                break # Se for válido, sai do loop
                            except ValueError:
                                print("Erro: Altura inválida. Por favor, digite um número.")
                        while True:
                            try:
                                peso = float(input('digite novo peso do pokemon: '))
                                break # Se for válido, sai do loop
                            except ValueError:
                                print("Erro: Peso inválido. Por favor, digite um número.")

                        CRUD_proxy.atualizar(id,nome,tipo,genero,altura,peso)
                    else :
                        print('ID não encontrado. Atualização cancelada.')
            except ValueError:
                print("Erro: Entrada inválida. Por favor, verifique os valores digitados.")
        case '4':
            try:
                id = int(input('digite id do pokemon: '))
                resultado = CRUD_proxy.remover(id)
                if resultado:
                    print('id ' + str(id) + ' removido.')
                else:
                    print("Erro: Não foi possível remover o ID. Verifique se o ID existe.")
            except ValueError:
                print("Erro: ID inválido. Por favor, digite um número inteiro.")

        case '5':
            dados = CRUD_proxy.buscar()
            if dados is not None:
                for d in dados:
                    print(d)
            else:
                print('Dados não encontrados')