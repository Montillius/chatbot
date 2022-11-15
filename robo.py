from chatterbot import ChatBot
from difflib import SequenceMatcher

ACEITACAO = 0.70

def comparar_mensagens(mensagem, mensagem_candidata):
    confianca = 0.0
    
    if mensagem.text and mensagem_candidata:
        texto_mensagem = mensagem.text
        texto_texto_mensagem_candidata = mensagem_candidata.text
        
        confianca = SequenceMatcher(
            None,
            texto_mensagem,
            texto_texto_mensagem_candidata
        )
        confianca = round(confianca.ratio(),2)
        if confianca < ACEITACAO:
            confianca = 0.0
        else:
            print("Mensagem do usuário:", texto_mensagem,", Mensagem candidata:", mensagem_candidata, "nível de confiança:", confianca)
    return confianca

def selecionar_resposta(mensagem, lista_respostas, storage=None):
    resposta = lista_respostas[0]
    print("resposta:", resposta)
    
    return resposta

def executar_robo():
    robo = ChatBot("Robô de atendimento sobre Conceitos Matemáticos",
        read_only = True,
        statement_comparison_function = comparar_mensagens,
        response_selection_method = selecionar_resposta,
        logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}
                          ])
    
    while True:
        entrada = input('Digite aqui...\n')
        resposta = robo.get_response(entrada)
        if resposta.confidence > 0.7:
            print(resposta)
        else:
            print('Não possuo essa resposta.')
            print('Faça outra pergunta.')
            
            
if __name__ == '__main__':
    executar_robo()