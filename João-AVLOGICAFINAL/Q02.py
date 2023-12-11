# primeio receber o salário 
salário= float(input("digite seu salário"))
# calcular o novo salário, reajuste e o percentual 
if salário <= 400.00:
    reajuste =(salário * 15)/100
    novoSalario= salário + reajuste
    print(f"seu novo salário {novoSalario:.2f} e seu reajuste {reajuste:.2f}")
# aplicar o mesmo processo aos outros mudando a variavel do reajuste e a porcentagem
elif salário >= 400.01 and salário <= 800.00:
    reajuste2=( salário * 12)/100
    novoSalario= salário + reajuste2
    print(f"seu novo salário {novoSalario:.2f} e seu reajuste {reajuste2:.2f}")
# mudar o reajuste e verificar se está correto
elif salário >= 800.01 and salário<= 1200.00:
    reajuste3= ( salário * 10)/100
    novoSalario= salário + reajuste3
    print(f"seu novo salário {novoSalario:.2f} e seu reajuste {reajuste3:.2f}")
# ùltima condição usando o elif 
elif salário >= 1200.01 and salário <= 2000.00:
    reajuste4= ( salário * 7)/100
    novoSalario= salário + reajuste4
    print(f"seu novo salário {novoSalario:.2f} e seu reajuste {reajuste4:.2f}")
#condição usando o else
else:
    salário >= 2000.00
    reajuste5= ( salário * 4)/100
    novoSalario= salário + reajuste5
    print(f"seu novo salário {novoSalario:.2f} e seu reajuste {reajuste5:.2f}")








