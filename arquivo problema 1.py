import time

def cronometro():
    tempo_inicial = time.time()
    input("Pressione Enter para parar o cronômetro.")
    tempo_final = time.time()

    tempo_total = tempo_final - tempo_inicial
    minutos = int(tempo_total // 60)
    segundos = int(tempo_total % 60)

    print(f"Tempo total: {minutos} minutos e {segundos} segundos.")

cronometro()