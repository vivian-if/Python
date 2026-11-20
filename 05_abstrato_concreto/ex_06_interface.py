"""
Exercicio 06 | Interface: um contrato para familias diferentes.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie a interface Avaliavel, com avaliar(nota) e media(). Faca o
    Entregador cumpri-la e o Prato herdar de Produto e tambem
    cumprir Avaliavel. Escreva destaque(), que recebe pratos e
    entregadores misturados e mostra quem tem media 4.5 ou mais.

Rode:  python3 ex_06_interface.py
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


class Produto(ABC):
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def descricao(self) -> str:
        pass


class Prato(Produto, Avaliavel):          # primeiro a mae, depois o contrato
    def __init__(self, nome: str, preco: int, serve: int) -> None:
        super().__init__(nome, preco)
        self.serve = serve
        self.notas: list[int] = []

    def descricao(self) -> str:
        return f"{self.nome} (serve {self.serve})"

    def __str__(self) -> str:
        return f"prato {self.nome}"

    def avaliar(self, nota: int) -> None:
        self.notas.append(nota)

    def media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


class Entregador(Avaliavel):              # outra familia, mesmo contrato
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.notas: list[int] = []

    def __str__(self) -> str:
        return f"entregador {self.nome}"

    def avaliar(self, nota: int) -> None:
        self.notas.append(nota)

    def media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


def destaque(avaliaveis: list[Avaliavel]) -> None:
    for a in avaliaveis:
        if a.media() >= 4.5:
            print(f"  destaque: {a} (media {a.media():.1f})")


# --- demonstracao ----------------------------------------------------
feijoada = Prato("Feijoada", 4500, 2)
tapioca = Prato("Tapioca", 1500, 1)
joao = Entregador("Joao")

for nota in [5, 5, 4]:
    feijoada.avaliar(nota)
for nota in [3, 4]:
    tapioca.avaliar(nota)
for nota in [5, 4, 5, 5]:
    joao.avaliar(nota)

print(feijoada.descricao(), reais(feijoada.preco))   # ainda e Produto
print(f"medias: {feijoada.media():.1f}  {tapioca.media():.1f}  {joao.media():.1f}")
destaque([feijoada, tapioca, joao])                   # pratos e entregador juntos

# Tire o # da linha abaixo, rode e leia a mensagem:
# contrato = Avaliavel()
#   TypeError: Can't instantiate abstract class Avaliavel without an
#   implementation for abstract methods 'avaliar', 'media'

# --- por que assim ---------------------------------------------------
# Avaliavel nao tem atributos nem codigo: so diz QUE metodos quem a
# cumpre precisa ter, nao COMO. Prato tem uma mae (Produto), de quem
# herda nome, preco e o dever de ter descricao(); e cumpre um
# contrato (Avaliavel), que o obriga a ter avaliar() e media(). Nos
# parenteses, a mae vem primeiro e o contrato depois. destaque() so
# conhece Avaliavel, por isso aceita pratos e entregadores, que nao
# tem nenhum parentesco.
