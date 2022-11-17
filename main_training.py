from training import Training


if __name__ == "__main__":
    Training = Training()
    Training.iniciar()
    biblioteca = Training.bibliotecas()
    conversas = Training.carregar_dialogos(biblioteca)
    if conversas:
        Training.training_bot(conversas)
    