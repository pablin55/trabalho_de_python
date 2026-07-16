"""
Modelos de dados do Quiz de Futebol.
Como os dados ficam em memória, essas classes representam
as entidades principais: Jogador e Pergunta.
"""
#Define as classes do sistema, como Jogador e Pergunta, organizando a estrutura dos dados.
class Jogador:
    """Representa um participante do quiz."""

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.pontuacao = 0
        self.acertos = 0
        self.total_perguntas_respondidas = 0

    def registrar_resposta(self, correta: bool, pontos_por_acerto: int = 10):
        """Atualiza pontuação e contagem de acertos do jogador."""
        self.total_perguntas_respondidas += 1
        if correta:
            self.acertos += 1
            self.pontuacao += pontos_por_acerto

    def to_dict(self):
        """Facilita exibir o jogador nos templates HTML."""
        return {
            "id": self.id,
            "nome": self.nome,
            "pontuacao": self.pontuacao,
            "acertos": self.acertos,
            "total_perguntas_respondidas": self.total_perguntas_respondidas,
        }


class Pergunta:
    """Representa uma pergunta de futebol com alternativas."""

    def __init__(self, id, enunciado, alternativas, resposta_correta):
        """
        alternativas: lista de strings, ex: ["A) ...", "B) ...", "C) ...", "D) ..."]
        resposta_correta: índice (0 a 3) da alternativa correta na lista
        """
        self.id = id
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.resposta_correta = resposta_correta

    def verificar_resposta(self, indice_escolhido):
        return indice_escolhido == self.resposta_correta
