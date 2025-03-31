lista_depositos = []
lista_saques = []

DEPOSITAR = 0
SAQUE = 1
EXTRATO = 2
SAIR = 3
saldo = 5000
valor_retirado = 0
num_saques = 3
i = 0
j = 0
while True:
    opcao = int(input("[0] Depositar \n[1] Saque \n[2] Extrato\n[3] Sair \n:"))

    if(opcao == DEPOSITAR):
        valor_depositado = float(input("Escreva quanto quer depositar: "))
        if(valor_depositado > 0):
            saldo += valor_depositado
            lista_depositos.append(valor_depositado)
            print(lista_depositos)
            i += 1
            print(f"{i}")
    elif(opcao == SAQUE):
        if(num_saques > 0):
            num_saques -= 1
            valor_retirado = float(input("Escreva quanto quer sacar: "))
            if((valor_retirado <= 500) and (valor_retirado < saldo)):
                saldo -= valor_retirado
                lista_saques.append(valor_retirado)
                print(lista_saques)
                j += 1
            else:
                print("O valor ultrapassa o seu limite")
        else:
            print("Seu limite de transações foi atingido")
    
    elif(opcao == EXTRATO):

        print("########EXTRATO########")

        for item1 in (lista_depositos):
            print(f"Deposito: R$ {item1:.2f}")
        
        for item2 in (lista_saques):
            print(f"Saque: R$ {item2:.2f}")
            
        print("#######################")

        print(f"R$ {saldo:.2f}")
        
        print("#######################")

    elif(opcao == SAIR):
        print("Obriagado por usar nosso sistema bancário")
        break

    else:
        print("Operação Inválida")
