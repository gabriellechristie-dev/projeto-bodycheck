from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso", "baixo"
    elif imc < 24.9:
        return "Peso normal", "normal"
    elif imc < 29.9:
        return "Sobrepeso", "sobrepeso"
    else:
        return "Obesidade", "obesidade"


def ajuste_peso(peso, altura):
    imc_min = 18.5
    imc_max = 24.9

    peso_min = imc_min * (altura ** 2)
    peso_max = imc_max * (altura ** 2)

    if peso < peso_min:
        return f"Você precisa ganhar aproximadamente {peso_min - peso:.1f} kg para entrar na faixa saudável."
    elif peso > peso_max:
        return f"Você precisa perder aproximadamente {peso - peso_max:.1f} kg para entrar na faixa saudável."
    else:
        return "Você já está na faixa saudável."


@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    mensagem = ""
    ajuste = ""
    classe = ""

    if request.method == "POST":
        try:
            peso = float(request.form["peso"].replace(",", "."))
            altura = float(request.form["altura"].replace(",", "."))

            # normalização inteligente (cm → m)
            if altura > 3:
                altura = altura / 100

            if peso <= 0 or altura <= 0:
                raise ValueError("Valores inválidos")

            imc = round(calcular_imc(peso, altura), 2)
            mensagem, classe = classificar_imc(imc)
            ajuste = ajuste_peso(peso, altura)

        except:
            mensagem = "Valores inválidos. Verifique os dados."

    return render_template(
        "index.html",
        imc=imc,
        mensagem=mensagem,
        ajuste=ajuste,
        classe=classe
    )


@app.route("/healthz")
def health():
    return "ok"


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)