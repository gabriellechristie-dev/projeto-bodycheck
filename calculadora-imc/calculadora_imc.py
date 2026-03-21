# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura_str = input("Digite sua altura (m): ")   
altura_str = altura_str.replace(",", ".")       
altura = float(altura_str) # Formatação para usar altura com "," e "."                     

# Validação
if peso > 0 and altura > 0:
    # Calcula IMC
    imc = peso / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}")

    # Classificação e recomendação
    if imc < 18.5:
        ganhar = 18.5 * altura**2 - peso
        print(f"Você está abaixo do peso! Você precisa ganhar {ganhar:.2f} kg para entrar na faixa saudável.")
    elif 18.5 <= imc <= 24.9:
        print("Você está com o peso ideal!")
    elif 25 <= imc <= 29.9:
        perder = peso - 24.9 * altura**2
        print(f"Você está com sobrepeso! Você precisa perder {perder:.2f} kg para entrar na faixa saudável.")
    elif 30 <= imc <= 34.9:
        perder = peso - 24.9 * altura**2
        print(f"Você está com obesidade grau 1! Você precisa perder {perder:.2f} kg para entrar na faixa saudável.")
    elif 35 <= imc <= 39.9:
        perder = peso - 24.9 * altura**2
        print(f"Você está com obesidade grau 2! Você precisa perder {perder:.2f} kg para entrar na faixa saudável.")
    elif imc >= 40:
        perder = peso - 24.9 * altura**2
        print(f"Você está com obesidade grau 3! Você precisa perder {perder:.2f} kg para entrar na faixa saudável.")
else:
    print("Por favor, digite valores válidos!")


