import random

def jogar():
print("=== Jogo de Adivinhação ===")
while True:
numero_secreto = random.randint(1, 100)
tentativas = 0
print("Tente adivinhar o número entre 1 e 100.")
    while True:
        palpite = input("Digite seu palpite: ")
        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.\n")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break
if name == "main":
jogar()
