import random

tentativa_maxima = input("Escreva o limite máximo que você quer chutar o número: ")

if tentativa_maxima.isdigit():
    tentativa_maxima = int(tentativa_maxima)
    
    if tentativa_maxima <= 0:
        print("Digite um número maior que 0 da próxima vez") 
        quit ()  
        
else:
    print("Digite um numero da proxima vez!") 
    quit()
    
random_number = random.randint(0, tentativa_maxima)
count = 0

while tentativa_maxima != random_number:
    count += 1
    
    tentativa_usuario = input("Tente um numero: ")
    if tentativa_usuario.isdigit():
        tentativa_usuario = int(tentativa_usuario)
    else:
        print("Escreva um numero da proxima vez. ")
        continue
        
    if tentativa_usuario == random_number:
        print("Você acertou!")
        break
    elif tentativa_usuario > random_number:
        print("Digite um numero menor")
    else:
        print("Digite um numero maior")
        

print(f"Você acertou em {count} tentativa(s)") 
        