#CRIAR UM SISTEMA BANCARIO COM AS OPERAÇÕES: SACAR, DEPOSITAR E VISUALIZAR EXTRATO
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu) #VOU EXIBIR MEU MENU

    if opcao == "d": #QUANDO SELECIONADO A OPÇÃO D INICIAR O DEPOSITO
        print('Deposito')
        deposito = float(input('Qual o valor de depósito? ')) #ESTOU RECEBENDO O INPUT DO VALOR DE DEPOSITO

        if deposito > 0: #O VALOR DO DEPÓSITO PRECISA SER POSITIVO POR EX SE FOR -10 ELE VAI PARA A PRÓXIMA ETAPA DO PROGRAMA ELSE   
            saldo += deposito #DEFINI PARA RECEBER EM SALDO O DEPOSITO
            extrato += (f'\nDeposito: R$ {deposito:.2f}') #ADCIONAR O DEPOSITO NA VARIAVEL EXTRATO
            print(f"""Deposito no valor R$ {deposito:.2f} realizado com sucesso!
Seu novo saldo é R$ {saldo}""")
        
        else: #QUANDO É FEITO A TENTATIVA DE DEPOSITO DE UM VALOR INVÁLIDO
            print(f'Deposite um valor válido!')

    elif opcao == "s": #QUANDO SELECIONADO A OPÇÃO S INICIAR O SAQUE
        print('Saque')
        saque = float(input('Digite o valor do saque: ')) #ESTOU RECEBENDO O INPUT DO VALOR DE SAQUE

        if saque > saldo: #SE O SAQUE É MAIOR QUE O SALDO ENTÃO SALDO INDISPONÍVEL
            print(f"""Saldo indisponível, seu saldo atual é R$ {saldo}.
Refaça a operação!""")
                
        elif saque > limite: #SE O SAQUE É MAIOR QUE O LIMITE DE SAQUE ENTÃO SAQUE INDISPONÍVEL
            print('Saque acima do limite não permitido! Refaça a operação.')

        elif numero_saques >= LIMITE_SAQUES: #A CADA SAQUE FEITO ELE BUSCA O VALOR NA VARIÁVEL E COMPARA COM O LIMITE DE SAQUES DIARIOS, SE MAIOR VOCÊ EXCEDEU O LIMITE DE SAQUE
            print ('Você excedeu o limite de saques diarios!')
        
        elif saque > 0: #O VALOR DO SAQUE PRECISA SER POSITIVO POR EX SE FOR -10 ELE VAI PARA A PRÓXIMA ETAPA DO PROGRAMA ELSE
            saldo = saldo - saque #O SALDO VAI RETIRAR O VALOR SACADO
            extrato += (f'\nSaque: R$ {saque:.2f}') #ADCIONAR O SAQUE NA VARIAVEL EXTRATO
            print(f"Saque no valor R$ {saque} efetuado com sucesso, seu novo saldo é R$ {saldo}")

            numero_saques += 1 #A CADA SAQUE FEITO ELE ADCIONA MAIS 1 NA VARIÁVEL
        
        else: #QUANDO É FEITO A TENTATIVA DE SAQUE DE UM VALOR INVÁLIDO
            print('Valor informado inválido!')

    elif opcao == "e":
        print('\n============= Extrato =============')
        print('Sem transações' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===================================')

    elif opcao == "q":
        print('Obrigado por ser nosso cliente!')
        break

    else:
        print('opção inválida')