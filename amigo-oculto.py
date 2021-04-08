# encoding: UTF-8
import sys
import random
import time


numbers = '101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899'


# Definições

def space():
    space = 1000000*' '
    print(space)

def space_short():
    print(" ")
    print(" ")
    print(" ")

def space_tiny():
    print(" ")


def progress_bar(value, max, barsize):
   chars = int(value * barsize / float(max))
   percent = int((value / float(max)) * 100)
   sys.stdout.write("#" * chars)
   sys.stdout.write(" " * (barsize - chars + 2))
   if value >= max:
      sys.stdout.write("pronto. \n\n")
   else:
      sys.stdout.write("[%3i%%]\r" % (percent))
      sys.stdout.flush()

def carregamento():
    for i in range(8):
        progress_bar(i, 7, 50)
        time.sleep(1)



# O programa

def AmigoOculto():
    # Variáveis
    qts = 0
    num = 0
    y = 0
    lista = []
    lista_save = []


    # Coletar quantidade de pessoas
    qts = input('Quantas pessoas vão participar? ')

    verification = 0

    if (str(qts) in numbers) and (int(qts) != 0):
        num = int(qts)
        verification = 1

    while verification == 0:
        space_short()
        print('Digite uma resposta válida. Somente números.')
        qts = input('Quantas pessoas vão participar? ')
        if (str(qts) in numbers):
            num = int(qts)
            verification = 1


    qts = int(qts)

    # Função
    print("Digite o nome dos participantes abaixo.")

    space_short()

    while qts > 0:
        y += 1
        pessoa = str(input(f"{y}: "))
        lista.append(pessoa.upper())
        lista_save.append(pessoa.upper())
        qts -= 1

    space()



    # Tiragem de nomes

    carregamento()

    while num > 0:
        space_short()
        print('Digite seu nome e veja quem você tirou.')
        space_tiny()

        nome = str(input("Nome: "))
        while nome.upper() not in lista_save:
            nome = str(input("Digite seu nome como está na lista: "))

        tirada = random.choice(lista)

        # Verificação de nome
        while tirada.upper() == nome.upper():
            tirada = random.choice(lista)

        print(f"Você tirou: {tirada}")
        
        # Excluindo nome da lista
        lista.remove(tirada)
        num -= 1

        # Chamando próximo
        print(" ")
        print(" ")
        ok = input("Aperte ENTER para confirmar...")

        space()
    

    exit()



# Finalizando

def exit():

    reiniciar = input('Deseja FAZER NOVAMENTE? (1) para SIM e (2) para NÃO: ')

    if reiniciar == '1':
        space_short()
        AmigoOculto()
    elif reiniciar == '2':
        sys.exit()
    else:
        space_short()
        print('Opa! Responda exatamente o que foi proposto.')
        space_short()

        exit()




# Iniciando

space_short()

print('Vai começar o AMIGO OCULTO!')

space_short()

click = input('Clique ENTER para continuar...')

space_short()

AmigoOculto()