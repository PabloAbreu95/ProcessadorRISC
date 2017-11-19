import operacoes;
import manip_strings_listas


class Cpu:
    def __init__(self, ram,tam,L):
        self.ram = ram
        self.tam = tam
        self.lista = L
        #Registradores
        self.mq = '000000000000'
        self.ac = ''
        self.mbr = ''
        self.ibr = ''
        self.ir = ''
        self.pc = 0
        self.cdb()


    def cdb(self): #Ciclo de busca
        while(self.pc<len(self.lista)):
            if(self.ibr==''): #Ibr está vazia
                self.mar = self.pc
                self.mbr = self.ram.retorna_palavra(self.mar) #Pega a linha da posição MAR
                if(self.necessario_esquerda(self.ir)=='sim'):
                    self.ir,self.mar,instrucao,endereco = (self.mbr).split(" ")
                    self.ibr = instrucao+' '+endereco

                else:
                    lixo,lixo2,self.ir,self.mar = (self.mbr).split(" ")
                    self.ibr = ''
                    self.pc += 1
            else:
                self.ir,self.mar = (self.ibr).split(" ")
                self.pc = self.pc + 1
                self.ibr = ''
            self.dcd(self.ir)

    def dcd(self, opcode): #Decodificação
    #''''''''''''''''''''''''''''''''''''''''''#
    #''''''''' TRANSFERENCIA DE DADOS '''''''''#
    #''''''''''''''''''''''''''''''''''''''''''#
        if(opcode=='00001010'): #Transfere o conteúdo de MQ pra AC
            print("\n\nLOAD(MQ)")
            self.ac = self.mq
            self.imprime() #Imprime todos os dados


        elif(opcode=='00001001'): #Transfere o conteúdo do local de memória X para MQ
            print("\n\nLOAD MQ,M(X)")
            self.mq = self.mar
            self.imprime()

        elif(opcode=='00100001'): #Transfere o conteúdo de AC para o local de memória X
            print("STOR M(X)")
            self.mar = self.ac
            print(self.mar)
            self.imprime()

        elif(opcode=='00000001'): #Transfere M(X) para o AC
            print('LOAD M(X)')
            self.ac = self.mar
            self.imprime()

        elif(opcode=='00000010'): #Transfere o -|M(X)| para o AC
            print('LOAD -M(X)')
            if(self.mar[0]=='1'):
                self.mar = manip_strings_listas.alteraString(self.mar,'0',0)
            else:
                self.mar = manip_strings_listas.alteraString(self.mar, '1', 0)
            self.ac = self.mar
            self.imprime()

        elif(opcode=='00000011'): #Transfere o valor absoluto de M(X) para o AC
            print('LOAD |M(X)|')
            self.mar = manip_strings_listas.alteraString(self.mar,'0',0)
            self.ac = self.mar
            self.imprime()

        elif(opcode=='00000100'): #Transfere-|M(X)| para AC
            print('LOAD -|M(X)|')
            self.mar = manip_strings_listas.alteraString(self.mar,'1',0)
            self.ac = self.mar
            self.imprime()



    #''''''''''''''''''''''''''''''''''''''''#
    #''''''''' DESVIO INCONDICIONAL '''''''''#
    #''''''''''''''''''''''''''''''''''''''''#
        elif(opcode=='00001101'): #Apanha a próxima instrução da metade esquerda de M(X)
            print("JUMP M(X,0:19)")
            self.pc+=1
            self.mbr = self.ram.retorna_palavra(self.pc)
            self.ibr=''

        elif(opcode=='00001110'): #Apanha a próxima instrução da metade direita de M(X)
            print("JUMP M(X,20:39)")
            self.pc+=1
            self.mbr = self.ram.retorna_palavra(self.pc)
            lixo,lixo,a,b = self.ram.retorna_palavra(self.pc).split(' ')
            self.ibr = a+' '+b


    #''''''''''''''''''''''''''''''''''''''#
    #''''''''' DESVIO CONDICIONAL '''''''''#
    #''''''''''''''''''''''''''''''''''''''#
        elif(opcode=='00001111'): #Se o número no AC for não negativo, apanha a próxima instrução da metade esquerda de M(X)
            if(self.ac[0]=='0'):
                print("JUMP + M(X,09:19")
                self.pc+=1
                self.mbr = self.ram.retorna_palavra(self.pc)
                self.ibr=''

        elif(opcode=='00010000'): #Se o número no AC for não negativo, apanha a próxima instrução da metade direita de M(X)
            if (self.ac[0] == '0'):
                print("JUMP + M(X,20:39")
                self.pc+=1
                self.mbr = self.ram.retorna_palavra(self.pc)
                lixo,lixo,a,b = self.ram.retorna_palavra(self.pc).split(' ')
                self.ibr = a+' '+b

    #''''''''''''''''''''''''''''''''#
    #''''''''' ARITIMÉTICAS '''''''''#
    #''''''''''''''''''''''''''''''''#
        elif(opcode=='00000101'): #Soma M(X) a AC, colococa o resultado em AC
            print("ADD M(X")
            b1 = operacoes.Binario(self.mar, self.ac)
            self.ac = b1.soma
            self.imprime()

        elif(opcode=='00000111'): #Soma |M(X)| a AC, coloca o resultado em AC
            print('ADD |M(X)|')
            self.mar = manip_strings_listas.alteraString(self.mar,'0',0)
            b1 = operacoes.Binario(self.mar,self.ac)
            self.ac = b1.soma
            self.imprime()

        elif(opcode=='00000110'): #Subtrai M(X) de AC, coloca o resultado em AC
            print("SUB M(X))")
            b1 = operacoes.Binario(self.mar, self.ac)
            self.ac = b1.sub
            self.imprime()

        elif(opcode=='00001000'): #Subtrai |M(X)| de AC, coloca o resultado em AC
            print("SUB |M(X)|)")
            self.mar = manip_strings_listas.alteraString(self.mar,'0',0)
            b1 = operacoes.Binario(self.mar, self.ac)
            self.ac = b1.sub
            self.imprime()

        elif(opcode=='00001011'): #Multiplica M(X) por MQ, coloca os bits mais signifcativos do resultado em AC, coloca bits menos significativos em MQ
            print("MULT M(X)")
            b1 = operacoes.Binario(self.mar, self.mq)
            self.ac = b1.mult_mais
            self.mq = b1.mult_menos
            self.imprime()

        elif(opcode=='00001100'): #Divide AC por M(X), coloca o quociente em MQ e o resto em AC
            print("DIV M(X)")
            b1 = operacoes.Binario(self.ac, self.mar)
            self.ac = b1.div_resto
            self.mq = b1.div_quociente
            self.imprime()

        elif(opcode=='00010100'): #Multiplica o AC por 2, ou seja, desloca a esquerda uma posição de bit
            print("LSH")
            x = manip_strings_listas.desloca_esquerda(self.ac)
            self.ac = x
            self.imprime()

        elif(opcode=='00010101'): #Divide o AC por 2, ou seja, desloca uma posição a direita
            print("RSH M(X)")
            x =  manip_strings_listas.desloca_direita(self.ac)
            self.ac = x
            print(self.ac)
            self.imprime()


    #'''''''''''''''''''''''''''''''''''''''''''#
    #''''''''' MODIFICAÇÃO DE ENDEREÇO '''''''''#
    #'''''''''''''''''''''''''''''''''''''''''''#
        elif(opcode=='00010010'): # Substitui o campo de endereço da esquerda em M(X) por 12 bits mais a direita de AC
           print("STOR M(X,8:19)")
           self.ram.modificaEnderecoEsquerda(self.pc-1,self.ac)
           self.atualiza_lista()



        elif(opcode=='00010011'): # Substitui o campo de endereço da direita em M(X) por 12 bits mais a direita de AC
            print("STOR M(X,28:39)")
            self.ram.modificaEnderecoDireita(self.pc-1,self.ac)
            self.atualiza_lista()



    def necessario_esquerda(self,ir):
        if(ir=='00001110'):
            return 'nao'
        else:
            return 'sim'

    def imprime(self):
        print('AC  = %s\nMQ  = %s\nIR  = %s\nMAR = %s\nIBR = %s\n\n------------'
              %(self.ac,self.mq,self.ir,self.mar,self.ibr))

    def atualiza_lista(self):
        self.lista = self.ram.palavras
