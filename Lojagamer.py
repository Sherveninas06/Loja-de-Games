import time 

print("="*50)
print("Loja de Jogos".center(50))
print("="*50)
print('Antes de começarmos, por favor preencha abaixo algumas perguntas! \n')

nome=input('Digite seu nome:')
print(f"Olá {nome}, abaixo vou te mostrar as categorias que temos na loja. \n")
time.sleep(1)

escolha = 0
total = 0 
carrinho = []
desconto = 0 

while escolha < 1 or escolha >7:
    
    print("="*50)
    print("CATEGORIAS".center(50))
    print("="*50)
    print("1- Ação")
    print("2- RPG ")
    print("3- Esporte ")
    print("4- Corrida ")
    print("5- Sandbox ")
    print("6- Terror ")
    print("7- Indie ")

    escolha=int(input('Qual você quer escolher?'))
    
    if escolha == 1 :
        time.sleep(2)
        print('='*50)
        print("AÇÃO".center(50))
        print('='*50)

        print("Códigos |         Jogos                  |  Valor"  )
        print("  1.    | Grand Theft Auto V             | 119,90$" )
        print("  2.    | Red Dead Redemption 2          | 249,90$" )
        print("  3.    | DOOM Eternal                   | 159,90$" )
        print("  4.    | Marvel's Spider-Man Remastered | 249,90$" )

        resposta = input("\nDeseja escolher um jogo? (sim/nao): ").lower()

        if resposta == "sim":
            jogo = int(input("Escolha o jogo: "))

            if jogo == 1 :
                carrinho.append("Grand Theft Auto V")
                total += 119.90
            
            elif jogo == 2 :
                carrinho.append("Red Dead Redemption 2")
                total += 249.90
            
            elif jogo == 3 :
                carrinho.append("DOOM Eternal")
                total += 159.90

            elif jogo == 4 :
                carrinho.append("Marvel's Spider-Man Remastered")
                total += 249.90

            print("✅ Jogo adicionado ao carrinho!")
            

            ver_mais = input("\nDeseja ver outras categorias de jogos? (sim/nao): ").lower()
            if ver_mais == "sim":
                escolha = 0
                       
            else:
                print("\n🛒 Indo para o carrinho...")
                time.sleep(2)
        
        else:
            print("\n🛒 CARRINHO")

            for item in carrinho:
                print("-", item)

            print(f"\nSubtotal: R$ {total:.2f}")

    elif escolha == 2:

        print('='*50)
        print("RPG".center(50))
        print('='*50)

        print("Códigos |         Jogos                  |  Valor"  )
        print("  1.    | The Witcher 3: Wild Hunt       | 129,90$" )
        print("  2.    | Cyberpunk 2077                 | 199,90$" )
        print("  3.    | Elden Ring                     | 299,90$" )
        print("  4.    | Skyrim Special Edition.        | 149,90$" )

        resposta = input("\nDeseja escolher um jogo? (sim/nao): ").lower()

        if resposta == "sim":
            jogo = int(input("Escolha o jogo: "))

            if jogo == 1:
                carrinho.append('The Witcher 3: Wild Hunt')
                total += 129.90

            elif jogo == 2:
                carrinho.append('Cyberpunk 2077')
                total += 199.90

            elif jogo == 3:
                carrinho.append('Elden Ring')
                total += 299.90

            elif jogo == 4:
                carrinho.append('Skyrim Special Edition')
                total += 149.90

            print("✅ Jogo adicionado ao carrinho!")

            ver_mais = input("\nDeseja ver outras categorias de jogos? (sim/nao): ").lower()

            if ver_mais == "sim":
                escolha = 0
                       
            else:
                print("\n🛒 Indo para o carrinho...")
                time.sleep(2)
        
        else:
            print("\n🛒 CARRINHO")

            for item in carrinho:
                print("-", item)

            print(f"\nSubtotal: R$ {total:.2f}")

    
    elif escolha == 3:
        
        print('='*50)
        print("ESPORTE".center(50))
        print('='*50)

        print("Códigos |       Jogos       |  Valor"  )
        print("  1.    | EA Sport FC26     | 349,90$" )
        print("  2.    | NBA 2k26          | 299,90$" )
        print("  3.    | F1 25             | 299,90$" )

        resposta = input("\nDeseja escolher um jogo? (sim/nao): ").lower()

        if resposta == "sim":
            jogo = int(input("Escolha o jogo: "))

            if jogo ==1:
                carrinho.append('EA Sport FC26')
                total+= 349.90

            elif jogo ==2:
                carrinho.append('NBA 2k26')
                total += 299.90

            elif jogo == 3:
                carrinho.append('F1 25')
                total += 269.90

            print("✅ Jogo adicionado ao carrinho!")

            ver_mais = input("\nDeseja ver outras categorias de jogos? (sim/nao): ").lower()
            if ver_mais == "sim":
                escolha = 0
                       
            else:
                print("\n🛒 Indo para o carrinho...")
                time.sleep(2)

        else:
            print("\n🛒 CARRINHO")

            for item in carrinho:
                print("-", item)

            print(f"\nSubtotal: R$ {total:.2f}")

        
    elif escolha == 4:

        print('='*50)
        print("CORRIDA".center(50))
        print('='*50)

        print("Códigos |       Jogos             |  Valor"  )
        print("  1.    | Forza Horizon 5         | 249,90$" )
        print("  2.    | Need for Speed Unbound  | 199,90$" )
        print("  3.    | The Crew Motorfest      | 229,90$" )

        resposta = input("\nDeseja escolher um jogo? (sim/nao): ").lower()

        if resposta == "sim":
            jogo = int(input("Escolha o jogo: "))

            if jogo ==1 :
                carrinho.append('Forza Horizon 5')
                total += 249.90

            elif jogo == 2 :
                carrinho.append('Need for Speed Unbound')
                total += 199.90

            elif jogo == 3:
                carrinho.append('The Crew Motorfest')
                total += 229.90

            print("✅ Jogo adicionado ao carrinho!")

            ver_mais = input("\nDeseja ver outras categorias de jogos? (sim/nao): ").lower()
            if ver_mais == "sim":
                escolha = 0
                       
            else:
                print("\n🛒 Indo para o carrinho...")
                time.sleep(2)

        else:
            print("\n🛒 CARRINHO")

            for item in carrinho:
                print("-", item)

            print(f"\nSubtotal: R$ {total:.2f}")

    
    elif escolha ==  5:

        print('='*50)
        print("SANDBOX".center(50))
        print('='*50)

        print("Códigos |       Jogos         |  Valor"  )
        print("  1.    | Minecraft           | 149,90$" )
        print("  2.    | Terraria            | 32,90$" )
        print("  3.    | Stardew Valley      | 30,90$" )

        resposta = input("\nDeseja escolher um jogo? (sim/nao): ").lower()

        if resposta == "sim":
            jogo = int(input("Escolha o jogo: "))

            if jogo == 1 :
                carrinho.append('Minecraft')
                total += 149.90

            elif jogo == 2:
                carrinho.append('Terraria')
                total += 32.90

            elif jogo == 3:
                carrinho.append('Stardew Valley')
                total += 30.90

            print("✅ Jogo adicionado ao carrinho!")

            ver_mais = input("\nDeseja ver outras categorias de jogos? (sim/nao): ").lower()
            if ver_mais == "sim":
                escolha = 0
                       
            else:
                print("\n🛒 Indo para o carrinho...")
                time.sleep(2)

        else:
            print("\n🛒 CARRINHO")

            for item in carrinho:
                print("-", item)

            print(f"\nSubtotal: R$ {total:.2f}")


    elif escolha ==  6:

        print('='*50)
        print("TERROR".center(50))
        print('='*50)

        print("Códigos |       Jogos         |  Valor"  )
        print("  1.    | Resident Evil 4     | 199,90$" )
        print("  2.    | Dead Space          | 249,90$" )
        print("  3.    | Outlast             | 59,90$" )

        resposta = input("\nDeseja escolher um jogo? (sim/nao): ").lower()

        if resposta == "sim":
            jogo = int(input("Escolha o jogo: "))

            if jogo == 1:
                carrinho.append('Resident Evil 4')
                total += 199.90

            elif jogo == 2:
                carrinho.append('Dead Space')
                total += 249.90

            elif jogo == 3:
                carrinho.append('Outlast')
                total += 59.90

            print("✅ Jogo adicionado ao carrinho!")
            

            ver_mais = input("\nDeseja ver outras categorias de jogos? (sim/nao): ").lower()
            if ver_mais == "sim":
                escolha = 0
                       
            else:
                print("\n🛒 Indo para o carrinho...")
                time.sleep(2)

        else:
            print("\n🛒 CARRINHO")

            for item in carrinho:
                print("-", item)

            print(f"\nSubtotal: R$ {total:.2f}")

    elif escolha == 7:

        print('='*50)
        print("INDIE".center(50))
        print('='*50)

        print("Códigos |       Jogos      |  Valor"  )
        print("  1.    | Hollow Knight    | 46,90$" )
        print("  2.    | Hades            | 73,90$" )
        print("  3.    | Celeste          | 36,90$" )

        resposta = input("\nDeseja escolher um jogo? (sim/nao): ").lower()

        if resposta == "sim":
            jogo = int(input("Escolha o jogo: "))

            if jogo == 1:
                carrinho.append('Hollow Knight')
                total += 46.90

            elif jogo == 2:
                carrinho.append('Hades')
                total += 73.90

            elif jogo ==3 :
                carrinho.append('Celeste')
                total += 36.90

            print("✅ Jogo adicionado ao carrinho!")

            ver_mais = input("\nDeseja ver outras categorias de jogos? (sim/nao): ").lower()

            if ver_mais == "sim":
                escolha = 0
                       
            else:
                print("\n🛒 Indo para o carrinho...")
                time.sleep(2)

        else:
            print("\n🛒 CARRINHO")

            for item in carrinho:
                print("-", item)

            print(f"\nSubtotal: R$ {total:.2f}")
    
    else :
        print('Opção inválida')

# -----------------------------
# calcular desconto

if total < 100:
    desconto = 0

elif total <= 200:
    desconto = total * 0.05

elif total <= 400:
    desconto = total * 0.10

else:
    desconto = total * 0.15

# -----------------------------

valor_final = total - desconto

print("="*50)
print("NOTA FISCAL".center(50))
print("="*50)

print(f"Cliente: {nome}")

for item in carrinho:
    print("-", item)

print(f"\nSubtotal: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {valor_final:.2f}")

print("="*50)
print("OBRIGADO PELA COMPRA".center(50))
print("="*50)
