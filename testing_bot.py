import unittest
from bot import *


class TesteSaudacoes(unittest.TestCase):
    
    def setUp(self):
        self.bot = ChatBot("Robô de atendimento sobre Conceitos Matemáticos",
                           logic_adapters=[
                               {
                                   "import_path": "chatterbot.logic.BestMatch",
                                   }
                               ])
        
    def testar_oi_ola_tudo_bem_alou(self):
        print("------------------------------")
        saudacoes = ["oi", "olá", "alou", "tudo bem?"]
        for saudacao in saudacoes:
            print(f'Testando saudação {saudacao}')
            resposta = self.bot.get_response(saudacao)
            self.assertIn("oi, eu sou um robô de atendimento sobre conceitos matemáticos. como posso te ajudar?", resposta.text.lower())
        print("------------------------------")
        
    def testar_bom_dia_boa_tarde_boa_noite(self):
        print("------------------------------")
        saudacoes = ["bom dia", "boa tarde", "boa noite"]
        for saudacao in saudacoes:
            print(f'Testando saudação {saudacao}')
            resposta = self.bot.get_response(saudacao)
            self.assertIn(saudacao+"! eu sou um robô de atendimento sobre conceitos matemáticos. como posso te ajudar?", resposta.text.lower())
        print("------------------------------")
        
class TesteBase(unittest.TestCase):        
    def setUp(self):
        self.bot = ChatBot("Robô de atendimento sobre Conceitos Matemáticos",
                           logic_adapters=[
                               {
                                   "import_path": "chatterbot.logic.BestMatch",
                                   }
                               ])
    
    def testar_matematica(self):
        print("------------------------------")
        perguntas = ["O que é matemática?", "Pra que serve a matemática?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("a matemática é a ciência do raciocínio lógico e abstrato, que estuda quantidades, espaço e medidas, estruturas, variações e estatística.", resposta.text.lower())
        print("------------------------------")
        
    def testar_areas_matematica(self):
        print("------------------------------")
        perguntas = ["Uma curiosidade sobre matemática?", "Alguma curiosidade sobre a matemática", "Me diz alguma curiosidade sobre a matemática!"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("a palavra matemática é originada do grego ", resposta.text.lower())
            print("------------------------------")
            
    def testar_trabalho_matematica(self):
        print("------------------------------")
        perguntas = ["Onde trabalha o profissional de Matemática?", "Qual a carreira de alguém que estuda Matemática?", "Onde posso trabalhar?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("as principais áreas de atuação do profissional de matemática ", resposta.text.lower())
            print("------------------------------")
            
    def testar_conceitos_matematica(self):
        print("------------------------------")
        perguntas = ["Quais as definições você tem?", "Sobre quais definições você pode falar?", "Quais definições você possui?", "Quais conceitos você possui?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("no momento só possuo alguns conceitos sobre geometria, o que gostaria de saber?", resposta.text.lower())
            print("------------------------------")
        
    def testar_local_matematica(self):
        print("------------------------------")
        perguntas = ["Existe algum curso de matemática em Vitória da Conquista?", "Tem curso de Matemática em Vitória da Conquista?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("em vitória da conquista - bahia, existe o ", resposta.text.lower())
            print("------------------------------")
    
class TesteConceito(unittest.TestCase):
    # Nesta classe só tem um teste, por conta da quantidade de perguntas.
    def setUp(self):
        self.bot = ChatBot("Robô de atendimento sobre Conceitos Matemáticos",
                           logic_adapters=[
                               {
                                   "import_path": "chatterbot.logic.BestMatch",
                                   }
                               ])

    
    def testar_conceito_geometria(self):
        print("------------------------------")
        perguntas = ["O que é Geometria?", "Qual o conceito de Geometria?", "Qual a definição de Geometria?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("a geometria é uma das três grandes áreas da matemática, ao lado ", resposta.text.lower())
            print("------------------------------")
            
    def testar_conceito_reta(self):
        print("------------------------------")
        perguntas = ["O que é uma reta?", "Qual o conceito de reta?" , "Qual a definição de reta?" ]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("dados dois pontos, existe uma única reta que os contém. portanto, retas podem ser ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_semirreta(self):
        print("------------------------------")
        perguntas = ["O que é uma semi reta?", "Qual o conceito de semirreta?" , "Qual a definição de semi-reta?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("as semirretas fazem parte dos estudos da geometria ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_ponto(self):
        print("------------------------------")
        perguntas = ["O que é um ponto?", "Qual o conceito de ponto?", "Qual a definição de ponto?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("O ponto não possui forma nem dimensão. Isso significa que o ponto é um objeto ", resposta.text.lower())
            print("------------------------------")
            
    def testar_conceito_circulo(self):
        print("------------------------------")
        perguntas = ["O que é um círculo?", "Qual o conceito de cícrulo?" , "Qual a definição de cícrulo?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("a definição de círculo está intimamente ligada à definição de circunferência. ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_quadrado(self):
        print("------------------------------")
        perguntas = ["O que é um Quadrado?", "Qual o conceito de Quadrado?", "Qual a definição de Quadrado?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("trata-se de uma figura geométrica plana poligonal e convexa que possui quatro lados ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_triangulo(self):
        print("------------------------------")
        perguntas = ["O que é um triângulo?", "Qual o conceito de triângulo?", "Qual a definição de triângulo?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("o triângulo é um polígono de três lados. ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_paralelogramo(self):
        print("------------------------------")
        perguntas = ["O que é um Paralelogramo?", "Qual o conceito de Paralelogramo?", "Qual a definição de Paralelogramo?" ]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("paralelogramos são figuras geométricas que possuem apenas ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_tese(self):
        print("------------------------------")
        perguntas = ["O que é uma Tese?", "Qual o conceito de Tese?", "Qual a definição de Tese?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("tese é um assunto, um tema, ", resposta.text.lower())
            print("------------------------------")
            
            
            
    def testar_conceito_corolario(self):
        print("------------------------------")
        perguntas = ["O que é um Corolário?", "Qual o conceito de Corolário?", "Qual a definição de Corolário?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("corolário significa o resultado proveniente ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_plano(self):
        print("------------------------------")
        perguntas = ["O que é um Plano?", "Qual o conceito de Plano?", "Qual a definição de Plano?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("planos são figuras geométricas bidimensionais formadas pela reunião de infinitas retas,  ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_poligono_convexo(self):
        print("------------------------------")
        perguntas = ["O que é um polígono convexo?", "Qual o conceito de polígono convexo?", "Qual a definição de polígono convexo?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("um polígono é convexo quando todos os pontos de um segmento", resposta.text.lower())
            print("------------------------------")
            
    def testar_conceito_poligono(self):
        print("------------------------------")
        perguntas = ["O que é um polígono?", "Qual o conceito de polígono?", "Qual a definição de polígono?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("os polígonos são linhas fechadas formadas apenas por segmentos de reta que ", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_area(self):
        print("------------------------------")
        perguntas = ["O que é um área?", "Qual o conceito de área?", "Qual a definição de área?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("área é um conceito matemático que pode ser definida como quantidade de espaço bidimensional,", resposta.text.lower())
            print("------------------------------")
            
    def testar_conceito_perimetro(self):
        print("------------------------------")
        perguntas = ["O que é um perimetro?", "Qual o conceito de perimetro?", "Qual a definição de perimetro?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("perímetro é uma medida observada em figuras geométricas planas, isto é,", resposta.text.lower())
            print("------------------------------")
            
            
    def testar_conceito_volume(self):
        print("------------------------------")
        perguntas = ["O que é um volume?", "Qual o conceito de volume?", "Qual a definição de volume?"]
        for pergunta in perguntas:
            print(f'Testando pergunta {pergunta}')
            resposta = self.bot.get_response(pergunta)
            self.assertIn("do latim volūmen, o conceito de volume permite ", resposta.text.lower())
            print("------------------------------")
    
        
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()
    
    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))
    testes.addTest(carregador.loadTestsFromTestCase(TesteBase))
    testes.addTest(carregador.loadTestsFromTestCase(TesteConceito))
   
    executor = unittest.TextTestRunner()
    executor.run(testes)
