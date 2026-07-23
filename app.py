from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import Jogador
from perguntas_respostas import obter_perguntas

app = Flask(__name__)
app.secret_key = "chave-secreta-para-sessao"

# -----------------------------
# Banco em memória
# -----------------------------
jogadores = {}
proximo_id = 1
ranking_historico = []


@app.route("/")
def index():
    return render_template("cadastro.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    global proximo_id

    nome = request.form.get("nome", "").strip()

    if not nome:
        flash("Digite um nome válido.")
        return redirect(url_for("index"))

    if any(j.nome.lower() == nome.lower() for j in jogadores.values()):
        flash("Já existe um jogador com esse nome.")
        return redirect(url_for("index"))

    jogador = Jogador(id=proximo_id, nome=nome)
    jogadores[proximo_id] = jogador

    session["jogador_id"] = proximo_id

    # Sorteia as perguntas apenas uma vez
    session["perguntas"] = obter_perguntas()

    # Começa da primeira pergunta
    session["pergunta_atual"] = 0

    proximo_id += 1

    return redirect(url_for("quiz"))


@app.route("/quiz")
def quiz():

    perguntas = session.get("perguntas", [])
    indice = session.get("pergunta_atual", 0)

    if indice >= len(perguntas):
        return redirect(url_for("resultado"))

    pergunta = perguntas[indice]

    return render_template(
        "quiz.html",
        pergunta=pergunta,
        numero=indice + 1,
        total=len(perguntas)
    )


@app.route("/responder", methods=["POST"])
def responder():

    # Resposta escolhida pelo jogador (A, B, C ou D)
    resposta = request.form.get("resposta")

    # Recupera as perguntas e a pergunta atual
    perguntas = session.get("perguntas", [])
    indice = session.get("pergunta_atual", 0)

    pergunta = perguntas[indice]

    # Recupera o jogador
    jogador = jogadores[session["jogador_id"]]

    # Verifica se acertou
    acertou = resposta == pergunta["correta"]

    # Atualiza pontuação do jogador
    jogador.registrar_resposta(acertou)

    # Próxima pergunta
    session["pergunta_atual"] += 1

    # Acabou o quiz?
    if session["pergunta_atual"] >= len(perguntas):

        ranking_historico.append({
            "nome": jogador.nome,
            "pontuacao": jogador.pontuacao,
            "acertos": jogador.acertos
        })

        return redirect(url_for("resultado"))

    return redirect(url_for("quiz"))


@app.route("/resultado")
def resultado():

    jogador = jogadores.get(session["jogador_id"])

    return render_template(
        "resultado.html",
        jogador=jogador
    )

@app.route("/ranking")
def ranking():

    ranking = sorted(
        ranking_historico,
        key=lambda jogador: jogador["pontuacao"],
        reverse=True
    )

    return render_template(
        "ranking.html",
        ranking=ranking
    )

if __name__ == "__main__":
    app.run(debug=True)