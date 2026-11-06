"""
Exercicio 08 | Classe abstrata, interface e polimorfismo juntos.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Monte um pequeno painel do restaurante: Produto abstrato com
    Prato e Bebida; Prato tambem Avaliavel; Entregador Avaliavel.
    Imprima o cardapio, o total, e a media de tudo o que pode ser
    avaliado.

Rode:  python3 ex_08_juntando_tudo.py
"""

from abc import ABC, abstractmethod


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Avaliavel(ABC):                     # interface: so o contrato
    @abstractmethod
    def avaliar(self, nota: int) -> None:
        pass

    @abstractmethod
    def media(self) -> float:
        pass


class Produto(ABC):                       # abstrata: molde com codigo comum
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def descricao(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.descricao():<26} {reais(self.preco)}"


class Prato(Produto, Avaliavel):
    def __init__(self, nome: str, preco: int, serve: int) -> None:
        super().__init__(nome, preco)
        self.serve = serve
        self.notas: list[int] = []

    def descricao(self) -> str:
        return f"{self.nome} (serve {self.serve})"

    def avaliar(self, nota: int) -> None:
        self.notas.append(nota)

    def media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


class Bebida(Produto):                    # Produto, mas nao avaliavel
    def __init__(self, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(nome, preco)
        self.volume_ml = volume_ml

    def descricao(self) -> str:
        return f"{self.nome} ({self.volume_ml} ml)"


class Entregador(Avaliavel):
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.notas: list[int] = []

    def avaliar(self, nota: int) -> None:
        self.notas.append(nota)

    def media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


def total(produtos: list[Produto]) -> int:
    return sum(p.preco for p in produtos)


def media_geral(avaliaveis: list[Avaliavel]) -> float:
    medias: list[float] = [a.media() for a in avaliaveis]
    return sum(medias) / len(medias)


# --- demonstracao ----------------------------------------------------
feijoada = Prato("Feijoada", 4500, 2)
tapioca = Prato("Tapioca", 1500, 1)
suco = Bebida("Suco de caju", 800, 500)
joao = Entregador("Joao")
feijoada.avaliar(5)
tapioca.avaliar(4)
joao.avaliar(5)
joao.avaliar(3)

cardapio: list[Produto] = [feijoada, tapioca, suco]
for p in cardapio:                        # polimorfismo pela classe abstrata
    print(p)
print("total:", reais(total(cardapio)))

avaliaveis: list[Avaliavel] = [feijoada, tapioca, joao]
print(f"media geral: {media_geral(avaliaveis):.2f}")   # pela interface

# --- por que assim ---------------------------------------------------
# Cada recurso no seu papel: Produto e abstrata porque pratos e
# bebidas SAO produtos e dividem codigo; Avaliavel e interface
# porque pratos e entregadores SABEM ser avaliados, sem serem
# parentes. A feijoada aparece nas duas listas -- e um Produto e e
# um Avaliavel. As anotacoes list[Produto] e list[Avaliavel] dizem,
# so de olhar, qual dos dois papeis cada funcao usa.
