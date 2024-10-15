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


    
def cond(a):
 erro==1
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

def cond(a):
 erro==2
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

def cond(a):
 erro==3 
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

def cond(a):
 erro==4
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

def cond(a):
 erro==5
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

def cond(a):
 erro==6
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




# for caractere in pchave:
#     #for valid in caractere:
#         if caractere == lescolh:
#             print(lescolh, end='')
#         elif caractere!= lescolh:
#             print(' ___ ', end='' )


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

#def desFoc(erros):


# cont=0
# #while cont<=numC:
# for caractere in pchave:
#       for valid in lescolh:
#         if caractere == lescolh:
#             print(lescolh, end='')
#         elif caractere!= lescolh:
#             print(' ___ ', end='' )
#     print('   !!!  ESCOLHA UMA LETRA DE A à Z E BOA SORTE  !!!')

# TENT
# cont=0
# while cont< numC:
#     cont = cont + 1 
#     for caractere in lescolh:
#         if caractere == lescolh:
#             print(lescolh, end='')
#         elif caractere!= lescolh:
#             print(' ___ ', end='' )
        
#    # print('   !!!  ESCOLHA UMA LETRA DE A à Z E BOA SORTE  !!!')
