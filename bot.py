from chatterbot import ChatBot


class Bot:
    
    def __init__(self):
        self.execute_bot()
    
    def execute_bot(self):
        try:
            bot = ChatBot("Robô de atendimento sobre Conceitos Matemáticos")
            
            while True:
                entrada = input('Digite aqui...\n')
                resposta = bot.get_response(entrada)
                if resposta.confidence > 0.7:
                    print(resposta)
                else:
                    print('Não possuo essa resposta.')
                    print('Faça outra pergunta.')
        except Exception:
            raise Exception
