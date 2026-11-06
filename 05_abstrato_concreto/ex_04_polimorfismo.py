"""
Exercicio 04 | Polimorfismo: uma chamada, varias respostas.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Escreva imprimir_cardapio(), total() e filtrar_ate() recebendo
    list[Produto]. Depois acrescente Sobremesa e Combo e mostre que
    as tres funcoes continuam funcionando, sem nenhuma alteracao.

Rode:  python3 ex_04_polimorfismo.py
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


def imprimir_cardapio(cardapio: list[Produto]) -> None:   # escritas ANTES
    for p in cardapio:
        print(f"  {p.descricao():<34} {reais(p.preco)}")


def total(produtos: list[Produto]) -> int:
    return sum(p.preco for p in produtos)


def filtrar_ate(produtos: list[Produto], preco_maximo: int) -> list[Produto]:
    baratos: list[Produto] = []
    for p in produtos:
        if p.preco <= preco_maximo:
            baratos.append(p)  # noqa: PERF401
    return baratos


# --- classes novas: nada acima foi alterado --------------------------
class Sobremesa(Produto):
    def descricao(self) -> str:
        return f"{self.nome} (sobremesa)"


class Combo(Produto):
    def __init__(self, nome: str, produtos: list[Produto]) -> None:
        super().__init__(nome, sum(p.preco for p in produtos) * 90 // 100)
        self.produtos = produtos

    def descricao(self) -> str:
        return f"{self.nome} ({len(self.produtos)} itens, -10%)"


# --- demonstracao ----------------------------------------------------
feijoada = Prato("Feijoada", 4500, 2)
suco = Bebida("Suco de caju", 800, 500)
pudim = Sobremesa("Pudim", 900)
almoco = Combo("Almoco completo", [feijoada, suco, pudim])

print("cardapio de ontem:")
imprimir_cardapio([feijoada, suco])
print("cardapio de hoje:")
hoje: list[Produto] = [feijoada, suco, pudim, almoco]
imprimir_cardapio(hoje)
print("total de hoje:", reais(total(hoje)))
print("ate R$ 10,00:")
imprimir_cardapio(filtrar_ate(hoje, 1000))

# --- por que assim ---------------------------------------------------
# A linha p.descricao() e sempre a mesma, mas cada objeto responde
# do seu jeito: isso e polimorfismo. As tres funcoes foram escritas
# quando so existiam pratos e bebidas, usam so o que todo Produto
# tem, e funcionaram sem nenhuma alteracao com sobremesas e combos.
# Com polimorfismo, acrescentar um tipo novo e criar uma classe --
# nao e cacar ifs espalhados pelo programa. Compare com a escada de
# isinstance, que precisaria de um elif novo para cada classe.
