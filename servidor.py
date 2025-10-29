import banco
import Pyro5.server
import Pyro5.core
import Pyro5.api
import pokemon

@Pyro5.server.expose
class CRUD:

    def __init__(self):
        self.banco = banco.Banco()

    def adicionar(self, poke):
        id = self.banco.adicionar(poke.nome,poke.tipo,poke.genero,poke.altura,poke.peso)
        return id

    def buscar(self, id = None):
        if id is None:
            self.banco.buscarTudo()
            return self.banco.buscarTudo()
        else:
            dados = self.banco.buscar(id)
            return dados

    def remover(self, id):
        id = self.banco.remover(id)
        return id

    def atualizar(self, id, nome, tipo, genero, altura, peso):
        id = self.banco.atualizar(id,nome,tipo,genero,altura,peso)
        return id

def main():
    
    daemon = Pyro5.server.Daemon()
    c = CRUD()
    endereco = daemon.register(c)
    print('URI:',endereco)

    # pois recebe objetos
    Pyro5.api.register_dict_to_class("pokemon.Pokemon",
                                        pokemon.converterDicionario)
    # pois envia objetos
    Pyro5.api.register_class_to_dict(pokemon.Pokemon,
                                   pokemon.converterPokemonDicionario)

    ns = Pyro5.core.locate_ns()
    ns.register('crud',endereco)

    daemon.requestLoop()

if __name__ == '__main__': main()