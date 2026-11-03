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