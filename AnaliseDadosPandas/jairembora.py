import time 

eleicao = input('Aperte <enter> para iniciar a votação:\n')
while True:
    g = '\033[32m'
    y = '\033[33m'
    r = '\033[31;4;40m'
    eleicao = input('Digite o número do presidente correto para votar:\n')
    if eleicao == '22':
        msg= f'{g} ERRO {y} MACRO!!! {g} ESSE {y} PRESIDENTE {g} NÃO {y} É {g} ADEQUADO!{y} POR {g} FAVOR, {y} TENTE {g} NOVAMENTE!!! \033[m'
        print(msg)
        print('='.center(50,'='))
    elif eleicao == '13':
        print(r)
        print('Ta na hora do Jair\n'.upper())
        time.sleep(2)
        print('Ta na hora do Jaiiiiiiiiiiiiir\n'.upper())
        time.sleep(3)
        print('Já ir embora!!!!!!\n'.upper())
        break
    else:
        print('essa opção nem é válida')