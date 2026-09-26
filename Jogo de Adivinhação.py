from random import randint 

num1 = randint(1,5)
num2 = randint(1,10)
num3 = randint(1,20)

print("\n================================")
print("Bem-Vindo ao Jogo de Adivinhacao")
print("================================\n")

difi = int(input("Selecione a difuldade: 1 - Facil | 2 - Medio | 3 - Dificil\n"))

while True:
    if difi == 1:
        n = int(input("Digite um numero que voce acha que vai sair\nDe 1 ate 5\n"))
        print("E o numero era", num1)
        if n == num1:
            print("Parabens voce acertou o numero!!!")
            break
        else:
            print("Que pena voce errou!!\n\nQuer tentar novamente? (Y/N)")
            break
    elif difi == 2:
           n = int(input("Digite um numero que voce acha que vai sair\nDe 1 ate 10\n"))
           print("E o numero era", num2)
           if n == num2:
               print("Parabens voce acertou o numero!!!\n\nQuer tentar novamente? (Y/N)")
               break
           else:
               print("Que pena voce errou!![\n\nQuer tentar novamente? (Y/N)")
               break
    elif difi == 3:
            n = int(input("Digite um numero que voce acha que vai sair\nDe 1 ate 20\n"))
            print("E o numero era", num3)
            if n == num3:
                print("Parabens voce acertou o numero!!!\n\nQuer tentar novamente? (Y/N)")
                break
            else:
                print("Que pena voce errou!![\n\nQuer tentar novamente? (Y/N)")
                break