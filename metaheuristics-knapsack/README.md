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
```python
def grasp(lrc, tempo, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    ini = time.time()
    achouT = time.time()
    melhorFO = float("-inf") #obtendo valor infinito negativo
    lrc = int((lrc * numObj) / 100) #calculando o % da LRC com base nos objetos
    mSol = [0] * numObj
    while 1:
        sol = heuConAleGul(lrc, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
        sol = heuPrimeiraMelhora(sol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc) #busca local
        FO = calcFO(sol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
        if FO > melhorFO:
            mSol = sol
            melhorFO = FO
            achouT = time.time()
        fim = time.time()
        if fim <= (ini + tempo): #verifica se deve continuar executando
            continue
        else:
            break
    return mSol, (achouT - ini)
```
- [X]  Simulated Annealing
```python
def SimulatedAnnealing(samax, ti, tc, tx, solIni, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    # gerando a semente
    rand.seed()

    ini = time.time()
    achouT = time.time()
    #guarda a solucao inicial como a melhor
    mSol = solIni
    mFO = calcFO(mSol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
    # TODO: Sol Ini vazia
    # atribui a melhor solucao a sol atual
    sol = cpy.copy(mSol)
    FO = calcFO(sol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
    #inicializa a temperatura
    temp = ti
    while temp > tc:
        #enquanto a temperatura inicial e maior que a temp de congelamento
        for i in range(samax):
            #solucao vizinha inicia a partir da solucao atual
            vSol = cpy.copy(sol)
            #sorteia uma solucao vizinha
            vSol[rand.randint(0, numObj-1)] = rand.randint(0, numMoc)
            #calcula a FO da solucao vizinha
            vFO = calcFO(vSol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
            #calculando a variacao
            delta = FO - vFO
            
            if delta < 0:
                #se a variacao e negativa entao aceita
                sol = cpy.copy(vSol)
                if vFO > mFO:
                    #se a FO da vizinha e melhor que a FO da FO global aceita
                    mSol = cpy.copy(vSol)
                    achouT = time.time()
            else:
                if rand.random() < mat.exp(-(FO - vFO) / temp):
                    #se nao e melhor mas aceita piorar
                    sol = cpy.copy(vSol)
            
        #resfria a temperatura
        temp *= tx
        
    return mSol, (achouT - ini)
```      
- [X]  Tabu Search
```python
def buscaTabu(tempo, T, solIni, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    ini = time.time()
    achouT = time.time()
    qtd = 0
    lista = np.zeros([2, T])
    mSol = solIni
    #calcula a FO da solucao
    mFOGlobal = calcFO(mSol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
    sol = cpy.copy(mSol)
    while 1:
        #melhor vizinho
        mFO = float("-inf") #obtendo valor infinito negativo
        mO = -1
        mM = -1
        
        for i in range(numObj):
            moc = sol[i] #guarda a mochila atual do objeto
            for j in range(numMoc):
                #verificar a posicao da lista Tabu
                pos = -1
                aspirou = 0
                for k in range(T):
                    if lista[0, k] == i and lista[1, k] == j:
                        pos = k
                        break
            
                if pos == -1:
                    #a configuracao nao esta na lista tabu
                    sol[i] = j
                    FO = calcFO(sol, numObj, numMoc, vetValObj, vetPesObj,
                                   vetCapMoc)
                    if FO > mFO:
                        mO = i
                        mM = j
                        mFO = FO
                else:
                    #esta na lista tabu, mas a FO e melhor que a FO Global
                    sol[i] = j
                    FO = CF.calcFO(sol, numObj, numMoc, vetValObj, vetPesObj,
                                   vetCapMoc)
                    if FO > mFOGlobal:
                        #aspiracao por objetivo
                        mO = i
                        mM = j
                        mFO = FO
                        #salva um flag para nao incluir na lista tabu novamente
                        aspirou = 1
                        #ajustando para mochila original
                sol[i] = moc
                        
        #atualizando a lista Tabu
        if mO != -1:
            #algum vizinho foi aceito
            sol[mO] = mM #o objeto na posicao aceita recebe a melhor mochila
            FO = mFO #atualiza a FO
            if (aspirou == 0): #nao usou o criterio de aspiracao
                lista[0, qtd] = mO
                lista[1, qtd] = mM
                qtd += 1
                if qtd >= T:
                    qtd = 0
        else:
            #nenhum vizinho aceito
            sol[lista[0,0]] = lista[1,0] #realiza a aspiracao por default
            FO = calcFO(sol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
        
        if FO > mFOGlobal:
            mSol = cpy.copy(sol)
            achouT = time.time()

        fim = time.time()
        #verifica se deve continuar executando
        if fim <= (ini + tempo):
            continue
        else:
            break
    
    return mSol, (achouT - ini)
```      
