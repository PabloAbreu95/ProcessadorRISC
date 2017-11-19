import conversoes
import manip_strings_listas
class Binario:
    def __init__(self,binario1,binario2):

        ####Transforma as strings em listas a fim de remover o elemento ('\n'), evitando possiveis erros com as funções a seguir####
        binario1 = manip_strings_listas.transformaEmLista(binario1)
        if(binario1[len(binario1)-1]=='\n'):
            binario1.pop()
        binario2 = manip_strings_listas.transformaEmLista(binario2)
        if(binario2[len(binario2)-1]=='\n'):
            binario2.pop()

        ####Agora transforma as listas em strings####
        binario1 = manip_strings_listas.transformaEmString(binario1)
        binario2 = manip_strings_listas.transformaEmString(binario2)

        #############
        ##'''''''''##
        ##Operações##
        ##'''''''''##
        #############

        self.decimal1 = int(conversoes.any2dec(binario1,2))
        self.decimal2 = int(conversoes.any2dec(binario2,2))


        #Soma
        soma = str(self.decimal1 + self.decimal2)
        soma = conversoes.dec2any(soma,2)
        tmp_soma = manip_strings_listas.transformaEmLista(soma)
        tmp_soma = manip_strings_listas.completaComZeros(tmp_soma)
        tmp_soma = manip_strings_listas.transformaEmString(tmp_soma)

        #Multiplica
        mult = str(self.decimal1 * self.decimal2)
        mult = conversoes.dec2any(mult,2)
        tmp_mult = manip_strings_listas.transformaEmLista(mult)
        tmp_mult= manip_strings_listas.completaComZeros(tmp_mult)
        tmp_mult2= manip_strings_listas.completaComZeros24(tmp_mult)
        tmp_mult2 = manip_strings_listas.transformaEmString(tmp_mult2)
        tmp_mult = manip_strings_listas.transformaEmString(tmp_mult)

        #Subtrai
        sub = str(self.decimal1 - self.decimal2)
        sub = conversoes.dec2any(sub,2)
        tmp_sub = manip_strings_listas.transformaEmLista(sub)
        tmp_sub = manip_strings_listas.completaComZeros(tmp_sub)
        tmp_sub = manip_strings_listas.transformaEmString(tmp_sub)

        #Divide
        div = str(int(self.decimal1 / self.decimal2)) #Somente a parte inteira
        div = conversoes.dec2any(div,2)
        tmp_div = manip_strings_listas.transformaEmLista(div)
        tmp_div = manip_strings_listas.completaComZeros(tmp_div)
        tmp_div = manip_strings_listas.transformaEmString(tmp_div)

        div2 = str(int(self.decimal1 % self.decimal2)) #Resto
        div2 = conversoes.dec2any(div2,2)
        tmp_div2 = manip_strings_listas.transformaEmLista(div2)
        tmp_div2 = manip_strings_listas.completaComZeros(tmp_div2)
        tmp_div2 = manip_strings_listas.transformaEmString(tmp_div2)


        #####Resultados##### Obs: refatorar futuramente para que não sejam feitas  todas as operacoes de uma vez
        self.soma = tmp_soma
        self.mult = tmp_mult
        self.sub = tmp_sub
        self.div = tmp_div
        self.mult_mais = tmp_mult2[0:12] #parte mais significativa da multiplicacao
        self.mult_menos = tmp_mult2[12:24] #parte menos significativa da multiplicaco
        self.div_quociente = tmp_div #Quociente da divisão
        self.div_resto = tmp_div2 #parte menos significativa da divisão
