"""
Exercicio 02 | Classe abstrata: o molde que nao vira objeto.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Transforme Produto em uma classe abstrata, com descricao() como
    metodo abstrato. Crie Prato e Bebida implementando descricao() e
    mostre que nao e mais possivel criar um Produto 'generico'.
    Depois crie uma Sobremesa que esquece de implementar descricao()
    e veja o erro.

Rode:  python3 ex_02_classe_abstrata.py
"""

from abc import ABC, abstractmethod


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Produto(ABC):
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def descricao(self) -> str:
        pass  # sem corpo: cada filha escreve o seu


class Prato(Produto):
    def __init__(self, nome: str, preco: int, serve: int) -> None:
        super().__init__(nome, preco)
        self.serve = serve

    def descricao(self) -> str:
        return f"{self.nome} (serve {self.serve})"


class Bebida(Produto):
    def __init__(self, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(nome, preco)
        self.volume_ml = volume_ml

    def descricao(self) -> str:
        return f"{self.nome} ({self.volume_ml} ml)"


class Sobremesa(Produto):
    pass  # esqueceu descricao()


# --- demonstracao ----------------------------------------------------
feijoada = Prato("Feijoada", 4500, 2)
suco = Bebida("Suco de caju", 800, 500)
print(feijoada.descricao(), reais(feijoada.preco))
print(suco.descricao(), reais(suco.preco))

# Tire o # da linha abaixo, rode e leia a mensagem:
# coisa = Produto("Coisa", 1000)
#   TypeError: Can't instantiate abstract class Produto without an
#   implementation for abstract method 'descricao'
#   (em versoes antigas do Python o texto muda um pouco)

# A filha que esquece o combinado tambem nao vira objeto:
# pudim = Sobremesa("Pudim", 900)
#   TypeError: Can't instantiate abstract class Sobremesa without an
#   implementation for abstract method 'descricao'

# --- por que assim ---------------------------------------------------
# No cardapio so existem pratos e bebidas; um 'produto generico' nao
# faz sentido. Herdando de ABC e marcando descricao() com
# @abstractmethod, Produto vira um molde: guarda o que e comum (nome
# e preco) e obriga cada filha a completar o que falta. Tentar criar
# um Produto da erro na hora -- antes de ele circular pelo programa.
# A filha que esquece um metodo abstrato tambem e barrada na
# criacao, e nao no meio de um pedido.
