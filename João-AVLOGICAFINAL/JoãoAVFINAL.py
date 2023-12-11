#receber o salário 
salário= float(input("Digite o seu salário"))
# começar a criar as condições 
if salário <=2000.00:
    print ("você esta isento" )
# segunda condição 
elif salário >= 2000.01 and salário <= 3000.00:
     print(f"R$ {salário*(8/100):.2f}")
# terceira condição 
elif salário >= 3000.01 and salário <= 4500.00:
      print(f"R$ {salário*(18/100):.2f}")
# ultima condição
else:
     salário >= 4500.00
     print(f"R$ {salário*(28/100):.2f}")
     



    
     