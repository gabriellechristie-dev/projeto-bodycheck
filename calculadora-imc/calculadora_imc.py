def obter_dados():
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura_str = input("Digite sua altura (m): ")
        altura_str = altura_str.replace(",", ".")
        altura = float(altura_str)

        if peso > 0 and altura > 0:
            return peso, altura
        else:
            print("Valores devem ser maiores que zero.")
            return None

    except:
        print("Entrada inválida.")
        return None


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc, peso, altura):

    if imc < 18.5:
        ganhar = 18.5 * altura**2 - peso
        return f"Você está abaixo do peso! Precisa ganhar {ganhar:.2f} kg."

    elif 18.5 <= imc <= 24.9:
        return "Você está com o peso ideal!"

    elif 25 <= imc <= 29.9:
        perder = peso - 24.9 * altura**2
        return f"Você está com sobrepeso! Precisa perder {perder:.2f} kg."

    elif 30 <= imc <= 34.9:
        perder = peso - 24.9 * altura**2
        return f"Obesidade grau 1! Precisa perder {perder:.2f} kg."

    elif 35 <= imc <= 39.9:
        perder = peso - 24.9 * altura**2
        return f"Obesidade grau 2! Precisa perder {perder:.2f} kg."

    else:
        perder = peso - 24.9 * altura**2
        return f"Obesidade grau 3! Precisa perder {perder:.2f} kg."


# Programa principal
continuar = "s"

while continuar == "s":

    dados = obter_dados()

    if dados is not None:
        peso, altura = dados

        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")

        mensagem = classificar_imc(imc, peso, altura)
        print(mensagem)

    else:
        print("Falha na entrada dos dados.")

    continuar = input("Deseja calcular novamente? (s/n): ").lower().strip()

print("Programa encerrado")