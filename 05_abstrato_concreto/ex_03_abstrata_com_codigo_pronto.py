"""
Exercicio 03 | Classe abstrata tambem tem codigo pronto.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Na classe abstrata Produto, escreva __str__ e reajustar() como
    metodos comuns, usando o metodo abstrato descricao(). As filhas
    so completam a parte que falta.

Rode:  python3 ex_03_abstrata_com_codigo_pronto.py
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
        pass

    def reajustar(self, percentual: int) -> None:     # pronto, para todas
        self.preco += self.preco * percentual // 100

    def __str__(self) -> str:                         # usa o abstrato
        return f"{self.descricao():<28} {reais(self.preco)}"


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


# --- demonstracao ----------------------------------------------------
feijoada = Prato("Feijoada", 4500, 2)
suco = Bebida("Suco de caju", 800, 500)
print(feijoada)
print(suco)

suco.reajustar(10)
print(suco)               # o reajuste veio pronto da mae

# --- por que assim ---------------------------------------------------
# Abstrata nao quer dizer vazia. Produto escreve uma vez o que vale
# para todos -- reajustar() e __str__ -- e deixa em aberto so o que
# muda de um produto para outro. O __str__ chama descricao() sem
# saber qual sera: quem responde e a filha. Cada subclasse escreve
# um metodo e ganha o resto.
