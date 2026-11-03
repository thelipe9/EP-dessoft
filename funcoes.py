def define_posicoes(linha, coluna, orientacao, tamanho):


    posicoes = []
    i = 0


    if orientacao == 'vertical':

        while i < tamanho:



            posicoes.append([linha, coluna])

            linha +=1
            i += 1

    elif orientacao == 'horizontal':
    
        while i < tamanho:
    
            posicoes.append([linha, coluna])
    
            coluna += 1
            i += 1

    return posicoes

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if navio in frota:
        frota[navio].append(posicoes)
        
    
    else:
        frota[navio] = [posicoes]
        

    return frota

def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:

        tabuleiro[linha][coluna] = 'X'

    else:
        tabuleiro[linha][coluna] = '-'
    
    
    return tabuleiro

def posiciona_frota(frota):

    tabuleiro = [[0]*10 for i in range(10)]

    for navios in frota.values():

        for navio in navios: 

            for posicao in navio:

                linha = posicao[0]
                coluna = posicao[1]

                tabuleiro[linha][coluna] = 1

    return tabuleiro