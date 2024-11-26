#===============================================================================================
#PARTE 1
#                 jogo da forca

import os
os.system ('cls')

print("            #JOGO DA FORCA#   ")
print("\n ")
print('        ESCOLHA A PALAVRA DA VEZ!!!       ')
print('                                ')
print('                                ')

pchave=str(input("           ")).upper()

import os
os.system ('cls')
#===============================================================================================
#PARTE 2
letras_acertadas=[ '__' for letra in pchave]
lescolh=[]
enforcou=False
acertou=False
erro=0
print("                #JOGO DA FORCA#   ")
print("\n ")

numC=int(len(pchave))  # FUNÇÃO LEN, CONTA A QUANTIDADE DE LETRAS DE UMA STRING
print ("            ", (' ___ ' * numC))
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




while(not enforcou and not acertou):
    print(letras_acertadas)
    print('   !!!  ESCOLHA UMA LETRA DE A à Z E BOA SORTE  !!!')
    lescolh=str(input("           ")).upper()

    if(lescolh in pchave):
        index = 0

        for letra in pchave:
            if (lescolh==letra):
                letras_acertadas[index]=letra
            index += 1 

        else:
            erro+=1 
            print(cond(erro))
    enforcou = erro == 6 
    acertou = '__' not in letras_acertadas
if(acertou):
    print('PARABENS VOCE ACERTOU!!!')
    print('A PALAVRA CERTA E:',pchave)
else:
    print(' VOCE ERROU !!!')
    print('A PALAVRA CERTA E:',pchave)



        


print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")

