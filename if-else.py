salario = float(input("informe seu salario: "))

if salario <=1860:
    print("estagiario")
elif salario >1860 and salario <=2300:
    print("programador junior")
elif salario >2300 and salario <=4700:
    print("programador pleno")
elif salario >4700 and salario <=15000:
    print("programador senior")
else:
    print("gerente de projetos")