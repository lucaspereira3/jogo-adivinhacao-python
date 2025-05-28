# 🕵️ Jogo de Adivinhação de Números em Python

Um jogo simples em Python onde o usuário tenta adivinhar um número aleatório gerado pelo computador dentro de um intervalo definido. O programa dá dicas se o palpite é maior ou menor que o número secreto.

---

## 🚀 Como usar

1. Clone o repositório:
```
git clone https://github.com/rafaelmoreirax/jogo-adivinhacao-python.git
cd jogo-adivinhacao-python
```

2. Execute o script:
python3 jogo_adivinhacao.py


3. Siga as instruções no terminal para tentar adivinhar o número.

---

## 🛠️ Tecnologias

- Python 3 (biblioteca padrão)

---

## 📋 Funcionalidades

- Gera um número aleatório entre 1 e 100.
- Recebe palpites do usuário via terminal.
- Indica se o palpite é maior ou menor que o número secreto.
- Conta o número de tentativas até acertar.
- Permite jogar novamente após acertar.

---

## jogo_adivinhacao.py
```
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

```
---

## 📋 Exemplo de uso
```
=== Jogo de Adivinhação ===
Tente adivinhar o número entre 1 e 100.
Digite seu palpite: 50
Tente um número maior.
Digite seu palpite: 75
Tente um número menor.
Digite seu palpite: 63
Parabéns! Você acertou em 3 tentativas.

Quer jogar novamente? (s/n): n
Obrigado por jogar! Até a próxima.
```

---

## 🏷️ Tags

`python` `jogo` `adivinhação` `terminal` `simples` `iniciante` `diversão`

---

## 📜 Licença

MIT

---

## 🤝 Contribuição

Pull requests e issues são bem-vindos!

---

## 📞 Contato

Desenvolvido por [rafael moreira](https://github.com/rafaelmoreirax)

