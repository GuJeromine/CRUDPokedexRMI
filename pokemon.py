class Pokemon:

    def __init__(self, nome, tipo, genero, altura, peso, id = None):
        self.nome = nome
        self.tipo = tipo
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.id = id

def converterPokemonDicionario(poke:Pokemon):
    dicionario = {
        "__class__":"pokemon.Pokemon",
        "nome":poke.nome,
        "tipo":poke.tipo,
        "genero":poke.genero,
        "altura":poke.altura,
        "peso":poke.peso,
        "id":poke.id,
    }
    return dicionario

def converterDicionario(classname, dicionario:dict):
    dicionario = Pokemon(dicionario["nome"],dicionario["tipo"],
                   dicionario["genero"],dicionario["altura"],
                   dicionario["peso"],dicionario["id"])
    return dicionario