print('##########################')
print('##########################')
print('### CALCULADORA BÁSICA ###')
print('##########################')
print('##########################')

# Author: Leonardo Bolek

def adicao():
    while True:
        try:
            adicao_1 = int(input('Digite um número: '))
            adicao_2 = int(input('Digite outro número: '))
            adicao_3 = adicao_1 + adicao_2
            print(f'{adicao_1} + {adicao_2} = {adicao_3}')
            continuar = int(input('Você deseja continuar? (1) Sim | (2) Não '))
            if (continuar == 1):
                return escolha()
            else:
                break
        except ValueError:
            print('Por favor, digite um número! :)')


def subtracao():
    while True:
        try:
            subtracao_1 = int(input('Digite um número: '))
            subtracao_2 = int(input('Digite outro número: '))
            subtracao_3 = subtracao_1 - subtracao_2
            print(f'{subtracao_1} - {subtracao_2} = {subtracao_3}')
            continuar = int(input('Você deseja continuar? (1) Sim | (2) Não '))
            if (continuar == 1):
                return escolha()
            else:
                break
        except ValueError:
            print('Por favor, digite um número! :)')


def multiplicacao():
    while True:
        try:
            multiplicacao_1 = int(input('Digite um número: '))
            multiplicacao_2 = int(input('Digite outro número: '))
            multiplicacao_3 = multiplicacao_1 * multiplicacao_2
            print(f'{multiplicacao_1} x {multiplicacao_2} = {multiplicacao_3}')
            continuar = int(input('Você deseja continuar? (1) Sim | (2) Não '))
            if(continuar == 1):
                return escolha()
            else:
                break
        except ValueError:
            print('Por favor, digite um número! :)')

def divisao():
    while True:
        try:
            divisao_1 = float(input('Digite um número: '))
            divisao_2 = float(input('Digite outro número: '))
            divisao_3 = divisao_1 / divisao_2
            print(f'{divisao_1} / {divisao_2} = {divisao_3}')
            continuar = int(input('Você deseja continuar? (1) Sim | (2) Não '))
            if (continuar == 1):
                return escolha()
            else:
                break
        except ValueError:
            print('Por favor, digite um número! :)')

def escolha():
    while True:
        try:
            print('\n(1) Adição | (2) Subtração | (3) Multiplicação | (4) Divisão')
            escolha = int(input('\nEscolha a operação aritmética: \n'))
            if escolha == 1:
                return adicao()
            elif escolha == 2:
                return subtracao()
            elif escolha == 3:
                return multiplicacao()
            elif escolha > 3:
                return divisao()
            break
        except ValueError:
            print('Por favor, digite um número! :)')

print(escolha())

print('Isto fica feliz em servir! :)')