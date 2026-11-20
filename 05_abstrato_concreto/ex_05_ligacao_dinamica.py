"""
Exercicio 05 | Ligacao dinamica: como o Python escolhe o metodo.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Mostre que a versao de descricao() executada depende do objeto,
    e nao da anotacao da variavel nem da classe onde o metodo que
    chama foi escrito.

Rode:  python3 ex_05_ligacao_dinamica.py
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

    def etiqueta(self) -> str:                    # escrito na mae...
        return f"[{self.descricao()}]"            # ...chama o da filha


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
p: Produto = Bebida("Suco de caju", 800, 500)   # a anotacao diz Produto...
print(type(p).__name__)                         # ...mas o objeto e Bebida
print(p.descricao())                            # quem responde: Bebida

p = Prato("Feijoada", 4500, 2)                  # mesma variavel, outro objeto
print(p.etiqueta())                             # etiqueta da mae, descricao do prato

# --- por que assim ---------------------------------------------------
# O Python decide qual descricao() executar no momento da chamada,
# olhando para o objeto -- nao para a anotacao da variavel, nem para
# a classe onde etiqueta() foi escrita. Isso se chama ligacao
# dinamica, e e ela que faz o polimorfismo funcionar. Decidir antes
# de o programa rodar seria ligacao estatica; em Python, a escolha e
# sempre na hora.
