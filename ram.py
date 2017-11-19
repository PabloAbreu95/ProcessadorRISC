class Ram:
    def __init__(self):
        self.palavras = []
        arquivo = open('intrucoes.txt', 'r')
        for linha in arquivo:
            self.palavras.append(linha)

    def retorna_palavra(self,indice): #Retorna uma palavra com base em um índice
        palavra = self.palavras[indice]
        return palavra

    def modificaEnderecoEsquerda(self,x,y): #Modifica o endereco da esquerda, onde X é o contador do programa(pc) e Y é o AC
        ir,mar,lixo,lixo2 = (self.palavras[x]).split(' ')
        z = self.palavras[x].replace(mar,y,1)
        self.palavras[x] = z
        print('\nNova palavra: '+self.palavras[x])

    def modificaEnderecoDireita(self,x,y): #Modifica o endereco da direita, onde Y é o AC
        lixo1,lixo2,ir,mar = (self.palavras[x]).split(' ')
        z = self.palavras[x].replace(mar,y,1)
        self.palavras[x] = z
        print('\nNova palavra: '+self.palavras[x])
