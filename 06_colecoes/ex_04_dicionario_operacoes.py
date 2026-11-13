"""
Exemplo 04 | Dicionario (dict): as operacoes principais.

Programacao Orientada a Objetos | IFRN

Uma operacao por bloco: o comentario diz o que ela faz e o que deve
aparecer na tela. Rode e acompanhe linha a linha.

Dicionario: guarda PARES chave -> valor. Voce acha o valor pela CHAVE,
sem precisar percorrer nada. As chaves nao se repetem; os valores podem.

Rode:  python3 ex_04_dicionario_operacoes.py
"""

# --- criar: chave: valor, separados por virgula ------------------------
precos: dict[str, int] = {"feijoada": 4500, "suco": 800, "tapioca": 1500}
print(precos)                     # {'feijoada': 4500, 'suco': 800, 'tapioca': 1500}
print(len(precos))                # 3 -- quantos pares

# --- ler pela chave ---------------------------------------------------
print(precos["suco"])             # 800
# precos["pizza"]                 # KeyError: 'pizza' -- a chave nao existe
print(precos.get("suco"))         # 800
print(precos.get("pizza"))        # None -- get nao da erro
print(precos.get("pizza", 0))     # 0    -- e aceita um valor padrao

procurado = precos.get("pizza")
if procurado is None:             # o jeito de saber que o get nao achou
    print("pizza nao esta no cardapio")

# --- a chave existe? --------------------------------------------------
print("suco" in precos)           # True  -- o in olha as CHAVES
print("pizza" not in precos)      # True
print(800 in precos.values())     # True  -- para procurar um VALOR, use .values()

# --- incluir e alterar: a mesma sintaxe -------------------------------
precos["pudim"] = 900             # a chave nao existia: INCLUI
precos["suco"] = 850              # a chave ja existia: ALTERA
print(precos)                     # {..., 'suco': 850, ..., 'pudim': 900}
precos.update({"cafe": 500, "pudim": 950})   # varios de uma vez
print(precos)                     # {..., 'pudim': 950, 'cafe': 500}

# --- remover ----------------------------------------------------------
del precos["cafe"]                # apaga o par
removido = precos.pop("pudim")    # apaga e DEVOLVE o valor
print(removido)                   # 950
print(precos.pop("pizza", 0))     # 0 -- com padrao, nao da erro se faltar
print(precos)                     # {'feijoada': 4500, 'suco': 850, 'tapioca': 1500}

# --- chaves, valores e pares ------------------------------------------
print(list(precos.keys()))        # ['feijoada', 'suco', 'tapioca']
print(list(precos.values()))      # [4500, 850, 1500]
print(list(precos.items()))       # [('feijoada', 4500), ('suco', 850), ('tapioca', 1500)]
print(sum(precos.values()))       # 6850

# --- percorrer: tres jeitos -------------------------------------------
for nome in precos:               # 1) so as chaves
    print(nome)
for valor in precos.values():     # 2) so os valores
    print(valor)
for nome, valor in precos.items():   # 3) chave e valor juntos
    print(f"{nome}: {valor} centavos")

# --- valores podem ser outras colecoes --------------------------------
cardapio: dict[str, dict[str, int]] = {
    "feijoada": {"preco": 4500, "serve": 2},
    "tapioca": {"preco": 1500, "serve": 1},
}
print(cardapio["feijoada"])               # {'preco': 4500, 'serve': 2}
print(cardapio["feijoada"]["serve"])      # 2 -- uma chave depois da outra
cardapio["tapioca"]["preco"] = 1600       # altera dentro do dicionario de dentro
cardapio["tapioca"]["vegano"] = 1         # inclui dentro dele
print(cardapio["tapioca"])                # {'preco': 1600, 'serve': 1, 'vegano': 1}

bairros: dict[str, list[str]] = {"Lagoa Nova": ["Ana", "Bia"], "Tirol": ["Davi"]}
bairros["Tirol"].append("Caio")           # a lista de dentro muda normalmente
print(bairros)                            # {'Lagoa Nova': ['Ana', 'Bia'], 'Tirol': ['Davi', 'Caio']}

# --- esvaziar ---------------------------------------------------------
precos.clear()
print(precos)                     # {}
