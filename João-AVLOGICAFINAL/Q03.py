# O usuario digita a sua senha 
AcessoaSenha= int(input("digite a sua senha "))
#criar a variavel  senha 
senha= 2002
#Verificar se a senha colocada pelo usuário é a senha correta,se não for pedir a senha novamente
while AcessoaSenha != senha:
     print("Senha Invalida")
     AcessoaSenha = int(input( "digite sua senha "))
# senha correta acesso permitido
print("acesso permitido ")
