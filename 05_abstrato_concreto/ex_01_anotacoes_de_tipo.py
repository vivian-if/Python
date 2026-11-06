"""
Exercicio 01 | Anotacoes de tipo: dizendo o que se espera.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Escreva a classe Produto e as funcoes total() e mais_caro() com
    anotacoes de tipo em todos os parametros, retornos e atributos
    que comecam vazios. Depois mostre que o Python nao confere os
    tipos sozinho.

Rode:  python3 ex_01_anotacoes_de_tipo.py
"""


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome                  # o tipo ja vem do parametro
        self.preco = preco                # em centavos
        self.tags: list[str] = []         # comeca vazia: diga o que vai guardar

    def marcar(self, tag: str) -> None:   # -> None: nao devolve nada
        self.tags.append(tag)


def total(produtos: list[Produto]) -> int:
    soma: int = 0
    for p in produtos:
        soma += p.preco
    return soma


def mais_caro(produtos: list[Produto]) -> Produto:
    maior = produtos[0]
    for p in produtos:
        if p.preco > maior.preco:
            maior = p
    return maior


def dobro(x: int) -> int:
    return x * 2


# --- demonstracao ----------------------------------------------------
feijoada = Produto("Feijoada", 4500)
suco = Produto("Suco de caju", 800)
feijoada.marcar("prato do dia")

cardapio: list[Produto] = [feijoada, suco]
print("total:", reais(total(cardapio)))
print("mais caro:", mais_caro(cardapio).nome)
print("tags da feijoada:", feijoada.tags)

# As anotacoes nao sao conferidas na execucao:
print(dobro(21))          # 42
print(dobro("ab"))        # abab -- o Python nao reclama

# --- por que assim ---------------------------------------------------
# Anotacao de tipo e documentacao que o editor entende: quem le
# total(produtos: list[Produto]) -> int sabe o que entregar e o que
# recebe de volta, sem abrir a funcao. O VS Code usa essas anotacoes
# para completar nomes e mostrar o que cada funcao espera. Mas o
# Python nao as confere: dobro('ab') roda. Ninguem e obrigado a
# escreve-las, mas elas deixam o codigo mais facil de ler e de usar.
