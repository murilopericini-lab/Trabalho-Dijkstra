def criar_grafo():
    return {'vertices': [], 'matriz': []}

def inserir_vertice(grafo, v):
    if v not in grafo['vertices']:
        grafo['vertices'].append(v)
        for linha in grafo['matriz']:
            linha.append(0)
        grafo['matriz'].append([0] * len(grafo['vertices']))
        print(f"Vértice '{v}' inserido com sucesso.")
    else:
        print(f"O vértice '{v}' já existe.")

def inserir_aresta(grafo, origem, destino, peso, nao_direcionado=True):
    if origem not in grafo['vertices'] or destino not in grafo['vertices']:
        print("\nErro: Os vértices de origem e destino devem ser criados manualmente primeiro (Opção 1)!")
        return
    
    i1 = grafo['vertices'].index(origem)
    i2 = grafo['vertices'].index(destino)
    grafo['matriz'][i1][i2] = peso
    if nao_direcionado:
        grafo['matriz'][i2][i1] = peso
    print(f"Aresta entre '{origem}' e '{destino}' com peso {peso} inserida com sucesso.")

def exibir_grafo(grafo):
    if not grafo['vertices']:
        print("\nO grafo está vazio.")
        return
    print("\n--- Matriz de Adjacência (Pesos) ---")
    print("   " + " ".join(f"{v:>3}" for v in grafo['vertices']))
    for i, v in enumerate(grafo['vertices']):
        linha_str = " ".join(f"{str(x):>3}" for x in grafo['matriz'][i])
        print(f"{v}: {linha_str}")
    print("-")

def dijkstra(grafo, inicio, destino):
    if inicio not in grafo['vertices'] or destino not in grafo['vertices']:
        print("Erro: Vértice inicial ou de destino não existe no grafo.")
        return [], float('inf')

    n = len(grafo['vertices'])
    distancias = {v: float('inf') for v in grafo['vertices']}
    anteriores = {v: None for v in grafo['vertices']}
    processados = []

    distancias[inicio] = 0

    while len(processados) < n:
        nao_processados = {v: distancias[v] for v in grafo['vertices'] if v not in processados}
        if not nao_processados:
            break
        
        atual = min(nao_processados, key=nao_processados.get)
        
        if distancias[atual] == float('inf'):
            break
        if atual == destino:
            break
            
        processados.append(atual)
        idx_atual = grafo['vertices'].index(atual)

        for j in range(n):
            peso = grafo['matriz'][idx_atual][j]
            if peso > 0:
                vizinho = grafo['vertices'][j]
                if vizinho not in processados:
                    nova_dist = distancias[atual] + peso
                    if nova_dist < distancias[vizinho]:
                        distancias[vizinho] = nova_dist
                        anteriores[vizinho] = atual

    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = anteriores[atual]

    if distancias[destino] == float('inf'):
        return [], float('inf')

    return caminho, distancias[destino]

def main():
    grafo = criar_grafo()
    while True:
        print("\n MENU")
        print("1. Inserir Vértice")
        print("2. Inserir Aresta com Peso")
        print("3. Exibir Matriz")
        print("4. Executar Dijkstra")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            v = input("Digite o nome do vértice: ").strip()
            inserir_vertice(grafo, v)
        elif opcao == '2':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            try:
                peso = int(input("Digite o peso da aresta: ").strip())
                nd_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
                nd = True if nd_input != 'n' else False
                inserir_aresta(grafo, origem, destino, peso, nao_direcionado=nd)
            except ValueError:
                print("Erro: O peso deve ser um número inteiro.")
        elif opcao == '3':
            exibir_grafo(grafo)
        elif opcao == '4':
            inicio = input("Digite o vértice inicial: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            caminho, custo = dijkstra(grafo, inicio, destino)
            if custo == float('inf'):
                print(f"-> Não existe caminho entre {inicio} e {destino}.")
            else:
                print(f"-> Menor Caminho: {' -> '.join(caminho)}")
                print(f"-> Custo Total: {custo}")
        elif opcao == '0':
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()