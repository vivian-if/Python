"""
Exemplo 01 | Lista: as operacoes principais.

Programacao Orientada a Objetos | IFRN

Uma operacao por bloco: o comentario diz o que ela faz e o que deve
aparecer na tela. Rode e acompanhe linha a linha; depois mude os valores
e rode de novo.

Lista: guarda itens EM ORDEM, ACEITA REPETIDOS e PODE MUDAR.

Rode:  python3 ex_01_lista_operacoes.py
"""

itens: list[str] = ["feijoada", "suco", "tapioca"]
print(itens)                      # ['feijoada', 'suco', 'tapioca']
print(len(itens))                 # 3 -- quantos itens

# --- acessar pela posicao ---------------------------------------------
print(itens[0])                   # feijoada -- a primeira posicao e 0
print(itens[-1])                  # tapioca  -- negativo conta do fim
itens[1] = "suco de caju"         # a lista pode mudar: troca a posicao 1
print(itens)                      # ['feijoada', 'suco de caju', 'tapioca']

# --- fatiar: um pedaco da lista ---------------------------------------
print(itens[0:2])                 # ['feijoada', 'suco de caju'] -- do 0 ate ANTES do 2
print(itens[1:])                  # ['suco de caju', 'tapioca']  -- do 1 ate o fim
print(itens[:2])                  # ['feijoada', 'suco de caju'] -- do comeco ate antes do 2

# --- adicionar --------------------------------------------------------
itens.append("pudim")             # um item no FIM
print(itens)                      # [..., 'tapioca', 'pudim']
itens.insert(0, "agua")           # um item na POSICAO 0; os outros andam
print(itens)                      # ['agua', 'feijoada', ...]
itens.extend(["cafe", "bolo"])    # VARIOS itens no fim, de outra lista
print(itens)                      # [..., 'pudim', 'cafe', 'bolo']
itens += ["cocada"]               # o mesmo que extend, com +=
print(itens)                      # [..., 'bolo', 'cocada']

# --- remover ----------------------------------------------------------
itens.remove("agua")              # tira a PRIMEIRA ocorrencia desse valor
print(itens)                      # ['feijoada', 'suco de caju', ...]
# itens.remove("pizza")           # ValueError: o valor nao esta na lista
ultimo = itens.pop()              # tira o ULTIMO e devolve
print(ultimo)                     # cocada
segundo = itens.pop(1)            # tira o da POSICAO 1 e devolve
print(segundo)                    # suco de caju
del itens[0]                      # apaga a posicao 0, sem devolver nada
print(itens)                      # ['tapioca', 'pudim', 'cafe', 'bolo']

# --- buscar e contar --------------------------------------------------
print("pudim" in itens)           # True  -- esta na lista?
print("pizza" not in itens)       # True  -- NAO esta na lista?
print(itens.index("cafe"))        # 2     -- em que posicao esta?
# itens.index("pizza")            # ValueError: o valor nao esta na lista
pedidos: list[str] = ["suco", "cafe", "suco", "suco"]
print(pedidos.count("suco"))      # 3     -- quantas vezes aparece

# --- ordenar e inverter -----------------------------------------------
print(sorted(itens))              # ['bolo', 'cafe', 'pudim', 'tapioca'] -- NOVA lista
print(itens)                      # ['tapioca', 'pudim', 'cafe', 'bolo'] -- original intacta
itens.sort()                      # ordena A PROPRIA lista (nao devolve nada)
print(itens)                      # ['bolo', 'cafe', 'pudim', 'tapioca']
itens.sort(reverse=True)          # ordem decrescente
print(itens)                      # ['tapioca', 'pudim', 'cafe', 'bolo']
itens.reverse()                   # inverte a ordem atual, sem ordenar
print(itens)                      # ['bolo', 'cafe', 'pudim', 'tapioca']

# --- listas de numeros ------------------------------------------------
precos: list[int] = [4500, 800, 1500, 900]
print(sum(precos))                # 7700 -- soma
print(min(precos))                # 800  -- menor
print(max(precos))                # 4500 -- maior

# --- percorrer --------------------------------------------------------
for item in itens:                # um item por volta
    print("-", item)
for posicao, item in enumerate(itens):   # a posicao e o item juntos
    print(posicao, item)          # 0 bolo / 1 cafe / ...

# --- lista dentro de lista --------------------------------------------
mesas: list[list[str]] = [["feijoada", "suco"], ["tapioca"], ["pudim", "cafe"]]
print(mesas[0])                   # ['feijoada', 'suco'] -- a lista da mesa 0
print(mesas[0][1])                # suco -- a posicao 1 dentro da mesa 0
for mesa in mesas:                # um laco dentro do outro
    for item in mesa:
        print(item, end=" ")
    print()                       # feijoada suco / tapioca / pudim cafe

# --- copiar (e a pegadinha) -------------------------------------------
mesma = itens                     # NAO copia: os dois nomes apontam para a mesma lista
copia = itens.copy()              # copia de verdade
outra_copia = itens[:]            # tambem copia: a fatia inteira
itens.append("sorvete")
print(mesma)                      # [..., 'sorvete'] -- mudou junto!
print(copia)                      # sem 'sorvete'
print(outra_copia)                # sem 'sorvete'

# --- esvaziar ---------------------------------------------------------
itens.clear()                     # tira tudo
print(itens)                      # []
print(len(itens))                 # 0
