def transformaEmLista(str1): #Transforma uma string em uma lista
    lista = []
    for x in str1:
        lista.append(x)
    return lista

def transformaEmString(lista):
    str1 = ''
    for i in lista:
        if(i!=' ' and i!=',' and i!='[' and i!=']' and i!="'"):
            i = str(i)
            str1 = str1+ i
    return str1

def completaComZeros(lista):
    casasquefaltam = 12 - len(lista)
    for x in range(0,casasquefaltam):
        lista.insert(0,0)
    return lista

def completaComZeros24(lista): #Completa multiplicações com zero até chegar em 24(casos de multiplicação)
    casasquefaltam = 24 - len(lista)
    for x in range(0,casasquefaltam):
        lista.insert(0,0)
    return lista

def alteraString(string,valor,pos):
    tmp = []
    for i in string:
        tmp.append(i)
    tmp[pos] = valor
    stri = ''
    for i in tmp:
        stri+= i
    return stri

def desloca_direita(string): #Desloca os bits 1 posição pra esquerda
    tmp = []
    tamanho = len(string)
    tmp.append('0')
    for i in range(1,tamanho):
        tmp.append(string[i-1])
    tmp = transformaEmString(tmp)
    return tmp

def desloca_esquerda(string): #Desloca os bits 1 posição pra esquerda
    tmp = []
    tamanho = len(string)

    for i in range(1,tamanho):
        tmp.append(string[i])
    tmp.insert(len(tmp),'0')
    tmp = transformaEmString(tmp)
    return tmp
