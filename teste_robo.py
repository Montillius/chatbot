import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):
    
    def setUp(self):
        self.robo = ChatBot("Robô de atendimento sobre Conceitos Matemáticos",
                read_only = True,
                statement_comparison_function = comparar_mensagens,
                response_selection_method = selecionar_resposta,
                logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}]
                )
        
    def testar_oi_ola_alou_tudo_bem(self):
        print('--------------------------------------------------------')
        print('--------------- testando a saudação oi, ola, alou, tudo bem -----------------')
        
        saudacoes = ["oi", "olá", "alou", "tudo bem?"]
        for saudacao in saudacoes:
            resposta = self.robo.get_response(saudacao)
            self.assertIn("Oi, eu sou um robô de atendimento sobre Conceitos Matemáticos. Como posso te ajudar?", resposta.text)
   
   
    def testar_bom_dia_boa_tarde_boa_noite(self):
        print('--------------------------------------------------------')
        print('--------------- testando a saudação bom dia, boa tarde, boa noite -----------------')
        
        saudacoes = ["bom dia", "Bom dia!", "Oi, bom dia!", "boa tarde", "Boa tarde!","Oi, boa tarde!", "boa noite", "Boa noite!", "Oi, boa noite!"]
        for saudacao in saudacoes:
            print(f'testando saudação: {saudacao}')
            resposta = self.robo.get_response(saudacao)
            self.assertIn(saudacao + "! Eu sou um robô de atendimento sobre Conceitos Matemáticos. Como posso te ajudar?", resposta.text)
   
        
if __name__== '__main__':
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()
    
    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)