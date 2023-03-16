import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, no):
        if len(self.filhos) < 3:
            self.filhos.append(no)

    def __repr__(self):
        return str(self.valor)

class AgenteDFS:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.visitados = set()

    def buscar(self, no):
        self.visitados.add(no)

        if no.valor == self.objetivo:
            return no

        for filho in no.filhos:
            if filho not in self.visitados:
                resultado = self.buscar(filho)
                if resultado is not None:
                    return resultado

        return None

def obter_profundidade(no):
    if not no.filhos:
        return 1

    profundidades = [obter_profundidade(filho) for filho in no.filhos]
    return max(profundidades) + 1

# Exemplo de uso
raiz = No(1)
objetivo = 5

# Cria árvore
for i in range(2, 10):
    pai = raiz
    for j in range(2, i):
        if pai.filhos:
            pai = random.choice(pai.filhos)
        else:
            break
    num_filhos = random.randint(0, 3)
    for k in range(num_filhos):
        filho = No(random.randint(0, 20))
        pai.adicionar_filho(filho)

def imprimir_arvore(no, prefixo="", is_ultimo=True):
    print(prefixo + ("└──" if is_ultimo else "├──") + str(no.valor))
    prefixo += "    " if is_ultimo else "│   "
    for i, filho in enumerate(no.filhos):
        is_ultimo = (i == len(no.filhos)-1)
        imprimir_arvore(filho, prefixo, is_ultimo)

# Executa busca
agente = AgenteDFS(objetivo)
resultado = agente.buscar(raiz)

# Exibe resultado
if resultado is not None:
    print(f"Encontrado! Valor: {resultado.valor}")
else:
    print("Valor não encontrado!")

# Obter Profundidade
print(f"Objetivo: {objetivo}")
profundidade = obter_profundidade(raiz)
print(f"Profundidade da árvore: {profundidade}")

imprimir_arvore(raiz)