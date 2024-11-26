#===============================================================================================
#PARTE 1
#                 jogo da forca

import os
os.system('cls')

print("            #JOGO DA FORCA#   ")
print("\n ")
print('        ESCOLHA A PALAVRA DA VEZ!!!       ')
print('                                ')
print('                                ')

pchave = str(input("           ")).upper()
import os
os.system('cls')


def cond():
    print("\n ")
    print('       ___________________         ')
    print('       ||               \|/        ')
    print('       ||                |         ')
    print('       ||                       ')
    print('       ||                      ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print("\n ")
    print("\n ")


#===============================================================================================
#PARTE 2
letras_acertadas = [    '__' for letra in pchave]
lescolh = []
enforcou = False
acertou = False
erro = 0
print("                #JOGO DA FORCA#   ")
print("\n ")
cond()
numC = len(pchave)  # FUNÇÃO LEN, CONTA A QUANTIDADE DE LETRAS DE UMA STRING
print("            ", (' ___ ' * numC))
print("\n ")
print("\n ")



def cond1():
    print("\n ")
    print('       ___________________         ')
    print('       ||               \|/        ')
    print('       ||                |         ')
    print('       ||             ______          ')
    print('       ||            (◉ _ ◉ )       ')
    print('       ||                          ')
    print('       ||                       ')
    print('       ||                    ')
    print('       ||                   ')
    print('       ||                  ')
    print('       ||                ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print("\n ")
    print("\n ")

def cond2():
    print("\n ")
    print('       ___________________         ')
    print('       ||               \|/        ')
    print('       ||                |         ')
    print('       ||             ______          ')
    print('       ||            (◉ _ ◉ )       ')
    print('       ||                |          ')
    print('       ||                |          ')
    print('       ||                |         ')
    print('       ||                      ')
    print('       ||                       ')
    print('       ||                       ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print("\n ")
    print("\n ")

def cond3():
    print("\n ")
    print('       ___________________         ')
    print('       ||               \|/        ')
    print('       ||                |         ')
    print('       ||             ______          ')
    print('       ||            (◉ _ ◉ )       ')
    print('       ||                |          ')
    print('       ||              / |          ')
    print('       ||             /  |         ')
    print('       ||                      ')
    print('       ||                       ')
    print('       ||                       ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print("\n ")
    print("\n ")

def cond4():
    print("\n ")
    print('       ___________________         ')
    print('       ||               \|/        ')
    print('       ||                |         ')
    print('       ||             ______          ')
    print('       ||            (◉ _ ◉ )       ')
    print('       ||                |          ')
    print('       ||              / | \         ')
    print('       ||             /  |  \       ')
    print('       ||                      ')
    print('       ||                       ')
    print('       ||                       ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print("\n ")
    print("\n ")

def cond5():
    print("\n ")
    print('       ___________________         ')
    print('       ||               \|/        ')
    print('       ||                |         ')
    print('       ||             ______          ')
    print('       ||            (◉ _ ◉ )       ')
    print('       ||                |          ')
    print('       ||              / | \         ')
    print('       ||             /  |  \       ')
    print('       ||              /        ')
    print('       ||             /          ')
    print('       ||          <-|             ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print("\n ")
    print("\n ")

def cond6():
    print("\n ")
    print('       ___________________         ')
    print('       ||               \|/        ')
    print('       ||                |         ')
    print('       ||             ______          ')
    print('       ||            (x _ x )       ')
    print('       ||                |          ')
    print('       ||              / | \         ')
    print('       ||             /  |  \       ')
    print('       ||              /   \     ')
    print('       ||             /     \     ')
    print('       ||          <-|       |->      ')
    print('       ||                          ')
    print('       ||                          ')
    print('       ||                          ')
    print("\n ")
    print("\n ")


def mostrar_forca(erro):
    if erro == 1:
        import os
        os.system('cls')
        cond1()
    elif erro == 2:
        import os
        os.system('cls')
        cond2()
    elif erro == 3:
        import os
        os.system('cls')
        cond3()
    elif erro == 4:
        import os
        os.system('cls')
        cond4()
    elif erro == 5:
        import os
        os.system('cls')
        cond5()
    elif erro == 6:
        import os
        os.system('cls')
        cond6()

while not enforcou and not acertou:
    print(letras_acertadas)
    print('   !!! ESCOLHA UMA LETRA DE A à Z E BOA SORTE !!!')
    print('   SABEH QUAL A PALAVRA?  sim / nao')
    palavra=str(input(' ')).lower()
    if palavra =='sim':
        print(' DIGITE A PALAVRA:')
        tentativa=str(input(' ')).upper()
        if tentativa == pchave:
            print('==='*16)
            print('      PARABÉNS! VOCÊ ACERTOU!!!')
            print('      A PALAVRA CERTA É:', pchave)
            print('==='*16)
            break
        elif tentativa!= pchave:
            print('==='*16)
            print('      VOCÊ PERDEU!!!')
            print('      A PALAVRA CERTA É:', pchave)
            print('==='*16)
            break
    print('==='*16)
    print('  DIGITE A LETRA  ')       
    lescolh = str(input("           ")).upper()

    if lescolh in pchave:
        for index, letra in enumerate(pchave):
            if lescolh == letra:
                letras_acertadas[index] = letra
    else:
        erro += 1
        mostrar_forca(erro)

    enforcou = erro == 6
    acertou = '__' not in letras_acertadas

if acertou:
    print('      PARABÉNS! VOCÊ ACERTOU!!!')
    print('      A PALAVRA CERTA É:', pchave)
# else:
#     print('      VOCÊ PERDEU!!!')
#     print('      A PALAVRA CERTA É:', pchave)

print("\n " * 10)
