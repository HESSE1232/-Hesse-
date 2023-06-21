import tkinter as tk
from datetime import datetime

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cronômetro")

        self.label_tempo = tk.Label(janela, text="00:00:00", font=("Arial", 24))
        self.label_tempo.pack(padx=20, pady=20)

        self.botao_iniciar = tk.Button(janela, text="Iniciar", command=self.iniciar_cronometro)
        self.botao_iniciar.pack(pady=10)

        self.botao_parar = tk.Button(janela, text="Parar", command=self.parar_cronometro, state=tk.DISABLED)
        self.botao_parar.pack(pady=10)

        self.temporizador = None
        self.tempo_inicial = None

    def iniciar_cronometro(self):
        self.tempo_inicial = datetime.now()
        self.atualizar_cronometro()
        self.botao_iniciar.config(state=tk.DISABLED)
        self.botao_parar.config(state=tk.NORMAL)

    def parar_cronometro(self):
        if self.temporizador:
            self.janela.after_cancel(self.temporizador)
            self.temporizador = None
            self.botao_iniciar.config(state=tk.NORMAL)
            self.botao_parar.config(state=tk.DISABLED)

    def atualizar_cronometro(self):
        tempo_atual = datetime.now() - self.tempo_inicial
        tempo_formatado = tempo_atual.strftime("%H:%M:%S")
        self.label_tempo.config(text=tempo_formatado)
        self.temporizador = self.janela.after(1000, self.atualizar_cronometro)

janela = tk.Tk()
cronometro = Cronometro(janela)
janela.mainloop()