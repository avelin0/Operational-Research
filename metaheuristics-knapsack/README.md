# KNAPSACK - MH
Constructive Heuristics:
- [X] Aleatory
```python
def heuConstrutivaAleatoria(numObj, numMoc):
    # inicializando o vetor de solucao com o tamanho do numero de objetos
    sol = [0] * numObj
    for i in range(numObj):
        sol[i] = rand.randint(0, numMoc) # para cada objeto e sorteado em qual mochila ele sera alocado
    return sol
```

- [X] Greedy
```python
def heuConstrutivaGulosa(numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    sol = [0] * numObj
    vetPes = [0] * numMoc #este vetor e utilizado para armazenar o peso alocado em cada mochila
    vAuxInd = np.argsort(vetValObj)[::-1] #obtendo os indices dos objetos ordenados (descendente)
    for i in range(numObj): #percorrendo os objetos
        for j in range(1, numMoc):            
            if (vetPes[j-1] + vetPesObj[vAuxInd[i]]) <= vetCapMoc[j-1]: #verifica se o objeto cabe na mochila
                sol[vAuxInd[i]] = j
                vetPes[j-1] += vetPesObj[vAuxInd[i]]
                break #se alocou o objeto na mochila, sai
    return sol
```
- [X] Greedy Aleatory 
```python
def heuConAleGul(lrc, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    #montando a LRC
    vetAux = [0] * numObj
    vetVal = [0] * lrc
    vetLrc = [0] * lrc
    for i in range(lrc):
        obj = rand.randint(0, numObj-1)
        while vetAux[obj] == 1: #impede o sorteio de um numero repetido
            obj = rand.randint(0, numObj-1)
        vetLrc[i] = obj
        vetVal[i] = vetValObj[obj]
        vetAux[obj] = 1
    # inserir os objetos da LRC na mochila de forma gulosa
    # obtendo os indices dos objetos ordenados (descendente)
    vAuxIndLRC = np.argsort(vetVal)[::-1]
    sol = [0] * numObj
    vetPes = [0] * numMoc
    for i in range(lrc):
        for j in range(numMoc):
            if (vetPes[j] + vetPesObj[vetLrc[vAuxIndLRC[i]]]) <= vetCapMoc[j]:
                sol[vetLrc[vAuxIndLRC[i]]] = j
                vetPes[j] = vetPes[j] + vetPesObj[vetLrc[vAuxIndLRC[i]]]
                break
    # inserir os demais objetos na mochila de forma gulosa
    vAuxIndObj = np.argsort(vetValObj)[::-1]
    for i in range(numObj):
        if vetAux[vAuxIndObj[i]] == 0: #se verdadeiro, entao nao foi alocado
            for j in range(numMoc):
                if (vetPes[j] + vetPesObj[vAuxIndObj[i]]) <= vetCapMoc[j]:
                    sol[vAuxIndObj[i]] = j
                    vetPes[j] = vetPes[j] + vetPesObj[vAuxIndObj[i]]
                    break
    return sol
```

Improvement Heuristics:
- [X]  First Improvement
- [X]  Best Improvement

Metaheuristic:
- [X]  GRASP
- [X]  Simulated Annealing
- [X]  Tabu Search
