# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 19:42:01 2023
@title: grasp for knaps problem
@author: bruno
"""

import numpy as np
import random as rand
import time
import math as mat
import copy as cpy

rand.seed() #gerando a semente

ALFA = 1000

# --------------------------------------------------------------------------------
# Util
# --------------------------------------------------------------------------------
def leDados():
    numObj = numMoc = 0     #inicializando as variaveis
    valObj, pesObj, capMoc = [], [], []
    f = open(r"C:\Users\bruno\OneDrive\programacao\python\metaheuristicas-mochila\dadosMochila1.txt", "r")     #lendo os dados

    linha = f.readline() #lendo a primeira linha
    valores = linha.split()
    numObj = int(valores[0]) #lendo o numero de objetos
    numMoc = int(valores[1]) #lendo o numero de mochilas
    
    linha = f.readline() #lendo a segunda linha
    valores = linha.split() #lendo os valores dos objetos
    for val in valores:
        valObj.append(int(val))
    
    linha = f.readline() #lendo a terceira linha
    valores = linha.split() #lendo os pesos dos objetos
    for val in valores:
        pesObj.append(int(val))

    linha = f.readline() #lendo a quarta linha
    valores = linha.split()
    for val in valores: #lendo a capacidade das mochilas
        capMoc.append(int(val))
    f.close()
    return numObj, numMoc, valObj, pesObj, capMoc

def calcFO(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc):
    fo = 0
    vetPes = [0] * numMoc
    for i in range(numObj):
        if solucao[i] != 0: #calcula a FO dos objetos selecionados
            fo += valObj[i]
            vetPes[solucao[i]-1] += vetPesObj[i]
    for j in range(numMoc):
        if vetPes[j] > vetCapMoc[j]: #verifica se a capacidade da mochila foi excedida
            fo -= ALFA * (vetPes[j] - vetCapMoc[j]) #se verdadeiro penaliza a FO
    return fo

# --------------------------------------------------------------------------------
# Heuristicas
# --------------------------------------------------------------------------------

def heuConstrutivaAleatoria(numObj, numMoc):
    # inicializando o vetor de solucao com o tamanho do numero de objetos
    sol = [0] * numObj
    for i in range(numObj):
        sol[i] = rand.randint(0, numMoc) # para cada objeto e sorteado em qual mochila ele sera alocado
    return sol

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

def heuMelhorMelhora(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc):
    while 1:
        mFO = calcFO(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc) #obtem a FO da solucao atualAula 9. Heurísticas 131
        #inicializa as variaveis que vao armazenar. o controle de troca de objeto e mochila
        mO = -1
        mM = -1
        for i in range(numObj):
            mAtual = solucao[i] #guarda a mochila atual
            for j in range(numMoc):
                solucao[i] = j #altera a mochila e calcula a FO da nova solucao
                FOAtual = calcFO(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc)
                if FOAtual > mFO: #se melhorar entao guarda as posicoes
                    mO = i
                    mM = j
                    mFO = FOAtual            
            solucao[i] = mAtual #restaura a mochila atual
        if mO != -1: #se verdadeiro entao houve melhora
            solucao[mO] = mM #guarda a melhora que ocorreu
        else:
            break #se nao tem como mais melhorar, termina
    return solucao

def heuPrimeiraMelhora(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc):
    while 1:
        #obtem a FO da solucao atual
        mFO = calcFO(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc)
        #inicializa a variavel de controle da interrupcao da busca
        melhorou = False
        for i in range(numObj):
            mAtual = solucao[i] #guarda a mochila atual
        for j in range(numMoc):
            solucao[i] = j #altera a mochila e calcula a FO com a nova
            solucao
            FOAtual = calcFO(solucao, numObj, numMoc, valObj, vetPesObj,vetCapMoc)
        if FOAtual > mFO: #se melhorar entao guarda as informacoes
            melhorou = True #registra q melhorou
            mFO = FOAtual #guarda a melhor FO
            break #sai do laco de mochilas
        if melhorou:
            break #sai do laco de objetos
        else:
            solucao[i] = mAtual #restaura a mochila atual
        if not melhorou: #se nao melhorou interrompe
            break
    return solucao

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

# --------------------------------------------------------------------------------
# Metaheurísticas
# --------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------
def aciona_grasp():
    numObjetos = numMochilas = 0
    LRC = 50 #neste exemplo adotou-se uma LRC de 50% dos objetos
    tempoExec = 10 #neste exemplo adotou-se 10 segundos de tempo de execucao
    vetValoresObjetos = []
    vetPesosObjetos = []
    vetCapacidadeMochilas = []
    numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos, vetCapacidadeMochilas = leDados()
    
    # #obtendo uma solucao pela meta-heuristica GRASP
    sol, tempo = grasp(LRC, tempoExec, numObjetos, numMochilas, vetValoresObjetos,
                        vetPesosObjetos, vetCapacidadeMochilas)
    
    # #calculando a FO da solucao obtida
    FO = calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos, vetCapacidadeMochilas)
    
    print("Solucao: ", sol)
    print("FO: ", FO)
    print("Achou em: %.2f " % tempo)

def aciona_busca_tabu():
    numObjetos = numMochilas = 0
    T = 10 #neste exemplo adotou-se o tamanho de 10 a lista Tabu
    tempoExec = 10 #neste exemplo adotou-se 10 segundos de tempo de execucao
    vetValoresObjetos = []
    vetPesosObjetos = []
    vetCapacidadeMochilas = []
    numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos, vetCapacidadeMochilas = leDados()
    
    solIni = heuConstrutivaAleatoria(numObjetos, numMochilas)
    
    #obtendo uma solucao pela meta-heuristica Busca Tabu
    sol, tempo = buscaTabu(tempoExec, T, solIni, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos, vetCapacidadeMochilas)
    
    #calculando a FO da solucao obtida
    FO = calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos, vetCapacidadeMochilas)
    
    print("Solucao: ", sol)
    print("FO: ", FO)
    print("Achou em: %.2f " % tempo)

def aciona_simulated_annealing():
    numObjetos = numMochilas = 0
    vetValoresObjetos = []
    vetPesosObjetos = []
    vetCapacidadeMochilas = []
    numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos, vetCapacidadeMochilas = LD.leDados()
    
    solIni = heuConstrutivaAleatoria(numObjetos, numMochilas)
    
    samax = ((numMochilas + 1) * numObjetos) * 1
    tempInicial = 100
    tempCongelamento = 0.01
    txResfriamento = 0.975
    
    #obtendo uma solucao pela meta-heuristica Simulated annealing
    sol, tempo = SA.SimulatedAnnealing(samax, tempInicial, tempCongelamento,
                                        txResfriamento, solIni, numObjetos, numMochilas, vetValoresObjetos,
                                        vetPesosObjetos, vetCapacidadeMochilas)
    
    #calculando a FO da solucao obtida
    FO = CF.calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
                    vetCapacidadeMochilas)
    
    print("Solucao: ", sol)
    print("FO: ", FO)
    print("Achou em: %.2f " % tempo)
