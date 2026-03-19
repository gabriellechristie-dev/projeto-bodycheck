peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

n_valido = peso > 0 and altura > 0

if n_valido:
    imc = peso / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso!")
    elif imc < 25:
        print("Você está com o peso ideal!")
    elif imc < 30:
        print("Seu IMC indica sobrepeso!")
    else:
        print("Seu IMC indica obesidade!")
else:
    print("Por favor, digite valores válidos!")


