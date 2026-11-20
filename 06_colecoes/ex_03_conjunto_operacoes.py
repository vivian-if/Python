"""
Exemplo 03 | Conjunto (set): as operacoes principais.

Programacao Orientada a Objetos | IFRN

Uma operacao por bloco: o comentario diz o que ela faz e o que deve
aparecer na tela. Rode e acompanhe linha a linha.

Conjunto: NAO TEM ORDEM, NAO ACEITA REPETIDOS e PODE MUDAR.
Serve para perguntar "esta aqui?" e para comparar grupos.

Como o conjunto nao tem ordem, o print dele pode sair em qualquer ordem.
Por isso, aqui usamos sorted(...) so para mostrar os itens em ordem.

Rode:  python3 ex_03_conjunto_operacoes.py
"""

# --- criar: chaves, sem pares chave:valor ------------------------------
ingredientes: set[str] = {"feijao", "carne", "arroz", "feijao"}  # noqa: B033
print(sorted(ingredientes))       # ['arroz', 'carne', 'feijao'] -- o repetido sumiu
print(len(ingredientes))          # 3

# --- esta aqui? -------------------------------------------------------
print("carne" in ingredientes)    # True
print("peixe" not in ingredientes)  # True

# --- adicionar --------------------------------------------------------
ingredientes.add("couve")         # entra
ingredientes.add("arroz")         # ja estava: nada acontece
print(sorted(ingredientes))       # ['arroz', 'carne', 'couve', 'feijao']

# --- remover ----------------------------------------------------------
ingredientes.remove("couve")      # tira; se nao existir, da erro
# ingredientes.remove("peixe")    # KeyError: 'peixe'
ingredientes.discard("peixe")     # tira SE existir; se nao, nada acontece
ingredientes.discard("arroz")
print(sorted(ingredientes))       # ['carne', 'feijao']
qualquer = ingredientes.pop()     # tira e devolve UM item qualquer
print(qualquer in ["carne", "feijao"])   # True -- nao da para saber qual
ingredientes.clear()              # tira tudo
print(ingredientes)               # set()

# --- tirar repetidos de uma lista -------------------------------------
pedidos: list[str] = ["suco", "cafe", "suco", "agua", "cafe"]
diferentes: set[str] = set(pedidos)
print(sorted(diferentes))         # ['agua', 'cafe', 'suco']
print(len(diferentes))            # 3 bebidas diferentes pedidas

# --- conjunto vazio: cuidado com as chaves ----------------------------
vazio: set[str] = set()           # assim e um conjunto vazio
print(type(vazio))                # <class 'set'>
nao_e: dict[str, int] = {}        # assim e um DICIONARIO vazio
print(type(nao_e))                # <class 'dict'>

# --- comparar grupos --------------------------------------------------
prato: set[str] = {"arroz", "camarao", "coco", "pimenta"}
alergias: set[str] = {"camarao", "amendoim"}
extras: set[str] = {"coco", "limao"}

print(prato & alergias)           # {'camarao'} -- INTERSECAO: o que esta nos dois
print(sorted(prato | extras))     # ['arroz', 'camarao', 'coco', 'limao', 'pimenta']
                                  #    -- UNIAO: tudo, sem repetir
print(sorted(prato - alergias))   # ['arroz', 'coco', 'pimenta']
                                  #    -- DIFERENCA: do prato, tirando as alergias
print(sorted(prato ^ extras))     # ['arroz', 'camarao', 'limao', 'pimenta']
                                  #    -- o que esta em UM so dos dois
print({"arroz", "coco"} <= prato) # True -- esta tudo dentro do prato?
print({"arroz"}.issubset(prato))  # True -- o mesmo, com o nome do metodo

if prato & alergias:              # conjunto vazio conta como False
    print("atencao: o prato tem algo que o cliente nao pode comer")

# --- percorrer --------------------------------------------------------
for item in sorted(prato):
    print("-", item)
