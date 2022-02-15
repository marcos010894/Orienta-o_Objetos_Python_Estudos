class Pessoa:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
    
    def __str__(self) -> str:
        return self.name

    def __eq__(self, __o: object) -> bool: #operação de igualar a outros objetos 
        if not isinstance(__o, Pessoa): return False #isinstace compara o tipo entre objetos 
        return self.name == __o.name
    def __add__(self, __o: object) -> int:
        return self.idade + __o.idade

    def __comp__(self, __o: object) -> int:
        return self.idade - __o.idade

class Ser:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade

    def __add__(self, __o: object) -> int:
        return self.idade + __o.idade


    def __comp__(self, __o: object) -> int:
        return self.idade - __o.idade
    

pessoa = Pessoa('Marcos Machado!', 18)
pessoa1 = Ser('joão!', 25)
print(pessoa - pessoa1)