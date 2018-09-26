#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import random
import os

#Limpa a tela
os.system('clear')

print('Jogo jokenpo\n')

ops = {1:'Pedra', 2:'Papel', 3:'Tesoura'}

#gera um numero de 1 a 3
numero_index = random.randint(1, 3)

#Espera um valor de acodo com a mensagem do input
entrada = int(input( '''Digite uma opcao:
    [1] = Pedra
    [2] = Papel
    [3] = Tesoura\n>>> '''))

#Verificacoes
#Verifica se o usuario perdeu, ganhou ou empato
#de acordo com o número digitado pelo usuário e sorteado pelo computador
#sendo que cada número representa o que voce jogou
if numero_index == 2 and entrada == 1:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce perdeu')
    
elif numero_index == 1 and entrada == 2:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce ganhou')

elif numero_index == 1 and entrada == 3:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce perdeu')
    
elif numero_index == 3 and entrada == 1:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce ganhou')
    
elif numero_index == 3 and entrada == 2:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce perdeu')
    
elif numero_index == 2 and entrada == 3:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce ganhou')
    
elif numero_index == 1 and entrada == 1:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce empato')
    
elif numero_index == 2 and entrada == 2:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce empato')
    
elif numero_index == 3 and entrada == 3:
    print(f'O computador jogou {ops[numero_index]}')
    print('\nvoce empato')
    
elif entrada == 0:
    pass

else:
    print('\nVoce digitou algo errado')

