#Arquivo principal do projeto. Controla as rotas do Flask
#  recebe as requisições do usuário e executa a lógica do quiz.

'''Flask é um microframework em Python utilizado para criar aplicações web,
 gerenciando rotas, requisições e a renderização de páginas HTML.'''


from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import Jogador, Pergunta

app = Flask(__name__)
app.secret_key = "chave-secreta-para-sessao"  # necessário para usar session

# ---------------------------------------------------------
# "Banco de dados" em memória
# ---------------------------------------------------------
# Dicionário de jogadores cadastrados: {id: Jogador}
jogadores = {}

# Contador simples para gerar IDs únicos
proximo_id = 1

# Lista que vai guardar o histórico de partidas finalizadas (para o ranking)
# Cada item: {"nome": str, "pontuacao": int, "acertos": int}
ranking_historico = []


@app.route("/")
def index():
    # Sempre que abrir a página inicial, começamos um cadastro novo
    return render_template("cadastro.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    global proximo_id

    nome = request.form.get("nome", "").strip()

    # Validação: nome vazio
    if not nome:
        flash("Digite um nome válido para começar.")
        return redirect(url_for("index"))

    # Validação: nome duplicado entre jogadores ainda "ativos" nesta sessão de partidas
    if any(j.nome.lower() == nome.lower() for j in jogadores.values()):
        flash(f'Já existe um jogador chamado "{nome}" nesta partida. Escolha outro nome.')
        return redirect(url_for("index"))

    # Cria o jogador e guarda no "banco" em memória
    jogador = Jogador(id=proximo_id, nome=nome)
    jogadores[proximo_id] = jogador

    # Guarda na sessão do navegador qual é o jogador atual e em que pergunta ele está
    session["jogador_id"] = proximo_id
    session["pergunta_atual"] = 0

    proximo_id += 1

    return f"Jogador '{jogador.nome}' cadastrado com sucesso! (id={jogador.id}) — próximo passo: tela do quiz."


if __name__ == "__main__":
    app.run(debug=True)
