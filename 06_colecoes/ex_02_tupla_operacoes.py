"""
Exemplo 02 | Tupla: as operacoes principais.

Programacao Orientada a Objetos | IFRN

Uma operacao por bloco: o comentario diz o que ela faz e o que deve
aparecer na tela. Rode e acompanhe linha a linha.

Tupla: guarda itens EM ORDEM, ACEITA REPETIDOS e NAO PODE MUDAR.
Serve para dados que andam juntos e nao devem ser alterados.

Rode:  python3 ex_02_tupla_operacoes.py
"""

# --- criar: parenteses no lugar de colchetes ---------------------------
entrega: tuple[float, float] = (-5.7945, -35.2110)   # latitude e longitude
print(entrega)                    # (-5.7945, -35.211)
print(len(entrega))               # 2

tamanhos: tuple[str, ...] = ("P", "M", "G", "M")     # ... = quantos forem
print(tamanhos)                   # ('P', 'M', 'G', 'M')

# --- ler: igual a lista -----------------------------------------------
print(entrega[0])                 # -5.7945
print(tamanhos[-1])               # M
print(tamanhos[1:3])              # ('M', 'G') -- fatia tambem e tupla

# --- mudar: proibido --------------------------------------------------
# entrega[0] = 0.0
#   TypeError: 'tuple' object does not support item assignment
# Tambem nao existem append, insert, remove nem pop.

# --- buscar e contar --------------------------------------------------
print("G" in tamanhos)            # True
print("GG" not in tamanhos)       # True
print(tamanhos.index("G"))        # 2 -- em que posicao esta
print(tamanhos.count("M"))        # 2 -- quantas vezes aparece

# --- desempacotar: um nome para cada posicao --------------------------
latitude, longitude = entrega
print(latitude)                   # -5.7945
print(longitude)                  # -35.211

# --- percorrer --------------------------------------------------------
for tamanho in tamanhos:
    print("-", tamanho)

# --- converter entre lista e tupla ------------------------------------
lista: list[str] = list(tamanhos) # vira lista: agora pode mudar
lista.append("GG")
print(lista)                      # ['P', 'M', 'G', 'M', 'GG']
de_volta: tuple[str, ...] = tuple(lista)
print(de_volta)                   # ('P', 'M', 'G', 'M', 'GG')

# --- a tupla de um elemento so ----------------------------------------
um: tuple[int] = (10,)            # a VIRGULA e que faz a tupla
print(um, type(um))               # (10,) <class 'tuple'>
nao_e = (10)                      # sem virgula: so um numero entre parenteses
print(nao_e, type(nao_e))         # 10 <class 'int'>
