from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json


class Training:
    
    def __init__(self):
            biblioteca = self.bibliotecas()
            self.iniciar()
            dialogos = self.carregar_dialogos(biblioteca)
            self.training_bot(dialogos)

    def bibliotecas(self):
        try:
            biblioteca = [
                    "dicionario/saudacoes.json",
                    "dicionario/base.json",
                    "dicionario/conceitos.json"
                ]
            return biblioteca
        except Exception:
            raise Exception

    def iniciar(self):
        try:
            global bot
            global coach
            bot = ChatBot("Robô de atendimento sobre Conceitos Matemáticos")
            coach = ListTrainer(bot)
        except Exception:
            raise Exception
        
    def carregar_dialogos(self, biblioteca):
        try:
            dialogos = []
            for dicionario in biblioteca:
                with open(dicionario, "r") as arquivo:
                    dicionario_configurado = json.load(arquivo)
                    dialogos.append(dicionario_configurado["dialogo"])
                    arquivo.close()
            return dialogos
        except Exception:
            raise Exception

    def training_bot(self, dialogos):
        try:
            global coach

            for dialogo in dialogos:
                for mensagens_resposta in dialogo:
                    mensagens = mensagens_resposta["mensagens"]
                    resposta = mensagens_resposta["resposta"]

                    print("Treinando o robô para responder a: ", mensagens, "com a responsta: ", resposta)
                    for mensagem in mensagens:
                        coach.train([mensagem, resposta])
        except Exception:
            raise Exception
