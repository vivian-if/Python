"""
Exercicio 07 | Uma classe, dois contratos.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie a interface Rastreavel, com onde_esta(). Faca o Pedido
    cumpri-la e o Entregador cumprir Avaliavel e Rastreavel ao mesmo
    tempo. Escreva um painel que mostra onde esta cada coisa
    rastreavel.

Rode:  python3 ex_07_varias_interfaces.py
"""

from abc import ABC, abstractmethod


# --- solucao ---------------------------------------------------------
class Avaliavel(ABC):                     # interface: so o contrato
    @abstractmethod
    def avaliar(self, nota: int) -> None:
        pass

    @abstractmethod
    def media(self) -> float:
        pass


class Rastreavel(ABC):
    @abstractmethod
    def onde_esta(self) -> str:
        pass


class Entregador(Avaliavel, Rastreavel):  # cumpre os dois contratos
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.bairro = "base do restaurante"
        self.notas: list[int] = []

    def mover_para(self, bairro: str) -> None:
        self.bairro = bairro

    def avaliar(self, nota: int) -> None:
        self.notas.append(nota)

    def media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def onde_esta(self) -> str:
        return f"entregador {self.nome}: {self.bairro}"


class Pedido(Rastreavel):                 # so um contrato
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.etapa = "na cozinha"

    def avancar(self, etapa: str) -> None:
        self.etapa = etapa

    def onde_esta(self) -> str:
        return f"pedido {self.numero}: {self.etapa}"


def painel(rastreaveis: list[Rastreavel]) -> None:
    for r in rastreaveis:
        print("  ", r.onde_esta())


# --- demonstracao ----------------------------------------------------
joao = Entregador("Joao")
p101 = Pedido(101)
p102 = Pedido(102)

print("17h00")
painel([p101, p102, joao])

p101.avancar("a caminho")
joao.mover_para("Lagoa Nova")
joao.avaliar(5)
print("17h20")
painel([p101, p102, joao])
print(f"media do {joao.nome}: {joao.media():.1f}")

# --- por que assim ---------------------------------------------------
# O Entregador cumpre dois contratos: pode ser avaliado e pode ser
# rastreado. O Pedido cumpre so um. painel() so pede Rastreavel,
# entao aceita pedidos e entregadores juntos. Essa e a diferenca
# pratica para a classe abstrata: uma classe herda de uma mae so,
# mas pode cumprir quantos contratos fizer sentido.
