#Armazena o banco de perguntas e respostas do quiz.
import random
perguntas = [

{
    "pergunta": "Qual país conquistou mais títulos da Copa do Mundo?",
    "opcoes": ["A) Alemanha", "B) Argentina", "C) Brasil", "D) Itália"],
    "correta": "C"
},
{
    "pergunta": "Quantos jogadores cada equipe possui em campo no início de uma partida?",
    "opcoes": ["A) 9", "B) 10", "C) 11", "D) 12"],
    "correta": "C"
},
{
    "pergunta": "Qual jogador é conhecido como 'Rei do Futebol'?",
    "opcoes": ["A) Zico", "B) Pelé", "C) Romário", "D) Ronaldo"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo de 2022?",
    "opcoes": ["A) França", "B) Brasil", "C) Argentina", "D) Croácia"],
    "correta": "C"
},
{
    "pergunta": "Qual clube espanhol é conhecido como Merengue?",
    "opcoes": ["A) Barcelona", "B) Atlético de Madrid", "C) Sevilla", "D) Real Madrid"],
    "correta": "D"
},
{
    "pergunta": "Quem é o maior artilheiro da história da Seleção Brasileira?",
    "opcoes": ["A) Pelé", "B) Neymar", "C) Ronaldo", "D) Romário"],
    "correta": "B"
},
{
    "pergunta": "Em qual país surgiu o futebol moderno?",
    "opcoes": ["A) Brasil", "B) Alemanha", "C) Inglaterra", "D) Itália"],
    "correta": "C"
},
{
    "pergunta": "Qual competição reúne os melhores clubes da Europa?",
    "opcoes": ["A) Europa League", "B) Champions League", "C) Conference League", "D) Supercopa Europeia"],
    "correta": "B"
},
{
    "pergunta": "Qual é a duração de uma partida de futebol profissional, sem acréscimos?",
    "opcoes": ["A) 80 minutos", "B) 90 minutos", "C) 100 minutos", "D) 120 minutos"],
    "correta": "B"
},
{
    "pergunta": "Quem ganhou a Bola de Ouro de 2023?",
    "opcoes": ["A) Erling Haaland", "B) Lionel Messi", "C) Kylian Mbappé", "D) Kevin De Bruyne"],
    "correta": "B"
},
{
    "pergunta": "Qual clube brasileiro possui mais títulos da Copa Libertadores?",
    "opcoes": ["A) Flamengo", "B) São Paulo", "C) Santos", "D) Palmeiras"],
    "correta": "D"
},
{
    "pergunta": "Quem é conhecido como 'Fenômeno'?",
    "opcoes": ["A) Ronaldinho", "B) Ronaldo", "C) Romário", "D) Rivaldo"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção venceu a primeira Copa do Mundo, em 1930?",
    "opcoes": ["A) Brasil", "B) Argentina", "C) Uruguai", "D) Itália"],
    "correta": "C"
},
{
    "pergunta": "Qual é o nome do estádio do Barcelona?",
    "opcoes": ["A) Santiago Bernabéu", "B) Camp Nou", "C) Old Trafford", "D) Anfield"],
    "correta": "B"
},
{
    "pergunta": "Quantos pontos vale uma vitória no Campeonato Brasileiro?",
    "opcoes": ["A) 1", "B) 2", "C) 3", "D) 4"],
    "correta": "C"
},
{
    "pergunta": "Qual goleiro é o jogador com mais partidas pela Seleção Brasileira?",
    "opcoes": ["A) Marcos", "B) Taffarel", "C) Dida", "D) Cafu"],
    "correta": "D"
},
{
    "pergunta": "Quem é o maior artilheiro da história das Copas do Mundo?",
    "opcoes": ["A) Pelé", "B) Miroslav Klose", "C) Ronaldo", "D) Lionel Messi"],
    "correta": "B"
},
{
    "pergunta": "Qual clube inglês é conhecido como 'The Reds'?",
    "opcoes": ["A) Chelsea", "B) Manchester City", "C) Liverpool", "D) Arsenal"],
    "correta": "C"
},
{
    "pergunta": "Qual brasileiro ganhou mais Bolas de Ouro da FIFA?",
    "opcoes": ["A) Pelé", "B) Kaká", "C) Ronaldo", "D) Ronaldinho Gaúcho"],
    "correta": "C"
},
{
    "pergunta": "Quem marcou o gol do título da Copa do Mundo de 2014?",
    "opcoes": ["A) Thomas Müller", "B) Mario Götze", "C) Miroslav Klose", "D) Mesut Özil"],
    "correta": "B"
},
{
    "pergunta": "Qual clube revelou Lionel Messi ao futebol profissional?",
    "opcoes": ["A) Newell's Old Boys", "B) Barcelona", "C) PSG", "D) Inter Miami"],
    "correta": "B"
},
{
    "pergunta": "Qual é a cor tradicional do cartão de expulsão?",
    "opcoes": ["A) Amarelo", "B) Verde", "C) Azul", "D) Vermelho"],
    "correta": "D"
},
{
    "pergunta": "Qual país sediou a Copa do Mundo de 2014?",
    "opcoes": ["A) África do Sul", "B) Brasil", "C) Rússia", "D) Qatar"],
    "correta": "B"
},
{
    "pergunta": "Quem é o maior campeão da UEFA Champions League?",
    "opcoes": ["A) Barcelona", "B) Bayern de Munique", "C) Real Madrid", "D) Milan"],
    "correta": "C"
},
{
    "pergunta": "Qual posição é responsável por defender o gol?",
    "opcoes": ["A) Zagueiro", "B) Atacante", "C) Goleiro", "D) Meio-campista"],
    "correta": "C"
},
{
    "pergunta": "Qual clube brasileiro é conhecido como Timão?",
    "opcoes": ["A) Palmeiras", "B) Corinthians", "C) Fluminense", "D) Grêmio"],
    "correta": "B"
},
{
    "pergunta": "Quem venceu a Copa América de 2021?",
    "opcoes": ["A) Brasil", "B) Uruguai", "C) Argentina", "D) Chile"],
    "correta": "C"
},
{
    "pergunta": "Qual jogador é conhecido como 'ET' pelos torcedores brasileiros?",
    "opcoes": ["A) Neymar", "B) Vini Jr.", "C) Ronaldinho", "D) Endrick"],
    "correta": "C"
},
{
    "pergunta": "Qual seleção é conhecida como La Albiceleste?",
    "opcoes": ["A) Espanha", "B) Argentina", "C) Uruguai", "D) Chile"],
    "correta": "B"
},
{
    "pergunta": "Qual brasileiro foi eleito melhor jogador do mundo em 2007?",
    "opcoes": ["A) Ronaldinho Gaúcho", "B) Kaká", "C) Ronaldo", "D) Neymar"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo Feminina de 2019?",
    "opcoes": ["A) Holanda", "B) Estados Unidos", "C) Alemanha", "D) Suécia"],
    "correta": "B"
},
{
    "pergunta": "Qual brasileira é considerada uma das maiores jogadoras da história do futebol feminino?",
    "opcoes": ["A) Cristiane", "B) Marta", "C) Formiga", "D) Debinha"],
    "correta": "B"
},
{
    "pergunta": "Quantas vezes Marta foi eleita a melhor jogadora do mundo pela FIFA?",
    "opcoes": ["A) 4", "B) 5", "C) 6", "D) 7"],
    "correta": "C"
},
{
    "pergunta": "Qual país sediou a Copa do Mundo Feminina de 2023?",
    "opcoes": ["A) França", "B) Austrália e Nova Zelândia", "C) Canadá", "D) Estados Unidos"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção conquistou a Copa do Mundo Feminina de 2023?",
    "opcoes": ["A) Inglaterra", "B) Espanha", "C) Suécia", "D) Estados Unidos"],
    "correta": "B"
},
{
    "pergunta": "Quem é a maior artilheira da história da Seleção Brasileira Feminina?",
    "opcoes": ["A) Cristiane", "B) Marta", "C) Formiga", "D) Bia Zaneratto"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção feminina possui mais títulos de Copa do Mundo?",
    "opcoes": ["A) Alemanha", "B) Estados Unidos", "C) Noruega", "D) Japão"],
    "correta": "B"
},
{
    "pergunta": "Em que ano ocorreu a primeira Copa do Mundo Feminina da FIFA?",
    "opcoes": ["A) 1987", "B) 1991", "C) 1995", "D) 1999"],
    "correta": "B"
},
{
    "pergunta": "Qual jogadora brasileira é conhecida pelo apelido de Rainha do Futebol?",
    "opcoes": ["A) Cristiane", "B) Marta", "C) Debinha", "D) Ary Borges"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção eliminou o Brasil na Copa do Mundo Feminina de 2023?",
    "opcoes": ["A) França", "B) Jamaica", "C) Suécia", "D) Canadá"],
    "correta": "B"
},
{
    "pergunta": "Qual competição reúne os principais clubes do futebol feminino da Europa?",
    "opcoes": ["A) Europa League Feminina", "B) Champions League Feminina", "C) Superliga Europeia", "D) Copa Feminina da UEFA"],
    "correta": "B"
},
{
    "pergunta": "Qual jogadora brasileira disputou mais Copas do Mundo Femininas?",
    "opcoes": ["A) Cristiane", "B) Marta", "C) Formiga", "D) Debinha"],
    "correta": "C"
},
{
    "pergunta": "Qual clube feminino brasileiro é um dos mais tradicionais do país?",
    "opcoes": ["A) Corinthians", "B) Flamengo", "C) Cruzeiro", "D) Fortaleza"],
    "correta": "A"
},
{
    "pergunta": "Qual país venceu a Copa do Mundo Feminina de 2007?",
    "opcoes": ["A) Brasil", "B) Alemanha", "C) Estados Unidos", "D) Suécia"],
    "correta": "B"
},
{
    "pergunta": "Quem marcou o gol do título da Espanha na final da Copa do Mundo Feminina de 2023?",
    "opcoes": ["A) Aitana Bonmatí", "B) Olga Carmona", "C) Jennifer Hermoso", "D) Salma Paralluelo"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo de 1994?",
    "opcoes": ["A) Brasil", "B) Itália", "C) Alemanha", "D) Argentina"],
    "correta": "A"
},
{
    "pergunta": "Quem foi o artilheiro da Copa do Mundo de 2014?",
    "opcoes": ["A) Thomas Müller", "B) James Rodríguez", "C) Lionel Messi", "D) Neymar"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo de 2006?",
    "opcoes": ["A) França", "B) Alemanha", "C) Itália", "D) Brasil"],
    "correta": "C"
},
{
    "pergunta": "Em qual país foi realizada a Copa do Mundo de 2002?",
    "opcoes": ["A) Japão e Coreia do Sul", "B) China", "C) Austrália", "D) Estados Unidos"],
    "correta": "A"
},
{
    "pergunta": "Quem foi eleito o melhor jogador da Copa do Mundo de 2006?",
    "opcoes": ["A) Cannavaro", "B) Pirlo", "C) Zidane", "D) Klose"],
    "correta": "C"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo de 1970?",
    "opcoes": ["A) Itália", "B) Brasil", "C) Alemanha Ocidental", "D) Uruguai"],
    "correta": "B"
},
{
    "pergunta": "Qual foi a primeira seleção africana a chegar a uma semifinal de Copa do Mundo?",
    "opcoes": ["A) Camarões", "B) Gana", "C) Marrocos", "D) Senegal"],
    "correta": "C"
},
{
    "pergunta": "Quem marcou o gol do título da Espanha na Copa de 2010?",
    "opcoes": ["A) David Villa", "B) Iniesta", "C) Xavi", "D) Torres"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo de 1978?",
    "opcoes": ["A) Brasil", "B) Alemanha Ocidental", "C) Argentina", "D) Holanda"],
    "correta": "C"
},
{
    "pergunta": "Quem foi o artilheiro da Copa do Mundo de 1998?",
    "opcoes": ["A) Ronaldo", "B) Davor Šuker", "C) Batistuta", "D) Zidane"],
    "correta": "B"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo de 1986?",
    "opcoes": ["A) Argentina", "B) Alemanha Ocidental", "C) Brasil", "D) França"],
    "correta": "A"
},
{
    "pergunta": "Em qual estádio foi disputada a final da Copa do Mundo de 2014?",
    "opcoes": ["A) Maracanã", "B) Mineirão", "C) Mané Garrincha", "D) Arena Corinthians"],
    "correta": "A"
},
{
    "pergunta": "Qual seleção venceu a Copa do Mundo de 1958?",
    "opcoes": ["A) Suécia", "B) Brasil", "C) França", "D) Alemanha"],
    "correta": "B"
},
{
    "pergunta": "Quem foi o artilheiro da Copa do Mundo de 2018?",
    "opcoes": ["A) Mbappé", "B) Harry Kane", "C) Lukaku", "D) Griezmann"],
    "correta": "B"
},
{
    "pergunta": "Qual país sediou a Copa do Mundo de 1998?",
    "opcoes": ["A) Itália", "B) Alemanha", "C) França", "D) Estados Unidos"],
    "correta": "C"
}

]
import random

def obter_perguntas(quantidade=10):
    return random.sample(perguntas, quantidade)