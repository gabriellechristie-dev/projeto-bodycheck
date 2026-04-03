from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):

    if imc < 18.5:
        return "Abaixo do peso"

    elif 18.5 <= imc <= 24.9:
        return "Peso ideal"

    elif 25 <= imc <= 29.9:
        return "Sobrepeso"

    elif 30 <= imc <= 34.9:
        return "Obesidade grau 1"

    elif 35 <= imc <= 39.9:
        return "Obesidade grau 2"

    else:
        return "Obesidade grau 3"


def calcular_ajuste(imc, peso, altura):

    peso_min = 18.5 * altura**2
    peso_max = 24.9 * altura**2

    if imc < 18.5:
        diff = peso_min - peso
        return f"Você precisa ganhar {diff:.2f} kg para entrar na faixa saudável."

    elif imc > 24.9:
        diff = peso - peso_max
        return f"Você precisa perder {diff:.2f} kg para entrar na faixa saudável."

    else:
        return "Você já está na faixa saudável."


@app.route("/", methods=["GET", "POST"])
def index():

    imc = None
    mensagem = None
    ajuste = None
    classe = None

    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])

        imc = calcular_imc(peso, altura)
        mensagem = classificar_imc(imc)
        ajuste = calcular_ajuste(imc, peso, altura)

        imc = round(imc, 2)

        if imc < 18.5:
            classe = "baixo"
        elif imc <= 24.9:
            classe = "normal"
        elif imc <= 29.9:
            classe = "sobrepeso"
        else:
            classe = "obesidade"

    return render_template(
        "index.html",
        imc=imc,
        mensagem=mensagem,
        ajuste=ajuste,
        classe=classe
    )


if __name__ == "__main__":
    app.run(debug=True)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)