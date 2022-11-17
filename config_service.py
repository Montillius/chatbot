from bot import *
from flask import Flask

VERSAO = "1.0"

bot = ChatBot("Robô de atendimento sobre Conceitos Matemáticos",
                read_only = True,
                logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}]
                )

servico_bot = Flask(__name__)

@servico_bot.route('/versao', methods=["GET"])
def get_versao():
    return VERSAO

@servico_bot.route('/resposta/<mensagem>', methods=["GET"])
def get_resposta(mensagem):
    resposta = bot.get_response(mensagem)
    return resposta.text

if __name__ == '__main__':
    servico_bot.run()