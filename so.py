import ram
import cpu
class SistemaOperacional:
    def __init__(self,tam):#Construtor da classe SO, parametro de entrada é um objeto da classe Ram
        self.ram = ram.Ram()
        self.cpu = cpu.Cpu(self.ram,tam,self.ram.palavras)
