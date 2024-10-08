def Somar(x,y):
    return x+y
def subtrair(x,y):
    return x-y
def multiplicar(x,y):
    return x*y
def dividir(x,y):
    return x/y
    
    if y !=0:
        return x/y
    else:
        return "Erro! Divisão por zero."
    
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = input("Digite o numero da operação (1/2/3/4):")
    
    num1 = float(input("Digite o primeiro numero:"))
    num1 = float(input("Digite o segundo numero:"))
    
    if escolha =='1':
        print(f"{num1}+{num1} = {add(num1,num2)}")
    else
