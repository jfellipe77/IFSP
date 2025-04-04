nome = input("Digite seu nome guerreiro: ")
escolha = input("Escolha sua arma (espada ou bastão): ").strip().lower()

if escolha == "espada":
    print(f"Amassou {nome}! Você acertou seu oponente com a sua espada!")
elif escolha == "bastão":
    print(f"Eita {nome}! Seu oponente acertou você com uma espada, você perdeu!")
else:
    print("O que?? Seu oponente derrotou você!")