from machine import Pin
from time import sleep

# ==========================
# CONTROLE DOS LEDS
# ==========================

led_verde = Pin(15, Pin.OUT)
led_amarelo = Pin(14, Pin.OUT)
led_vermelho = Pin(13, Pin.OUT)

# ==========================
# CENÁRIOS DA SPRINT
# ==========================

cenarios = [
    {
        "geracao": 4000,
        "consumo": 1500
    },
    {
        "geracao": 1800,
        "consumo": 1500
    },
    {
        "geracao": 1000,
        "consumo": 1800
    }
]

# ==========================
# LOOP PRINCIPAL
# ==========================

while True:

    for cenario in cenarios:

        geracao = cenario["geracao"]
        consumo = cenario["consumo"]

        disponivel = geracao - consumo

        led_verde.off()
        led_amarelo.off()
        led_vermelho.off()

        if disponivel >= 1000:

            status = "RECARGA AUTORIZADA"
            led_verde.on()

        elif disponivel >= 0:

            status = "RECARGA REDUZIDA"
            led_amarelo.on()

        else:

            status = "RECARGA BLOQUEADA"
            led_vermelho.on()

        print("\n===================================")
        print("CONTROLE INTELIGENTE DE RECARGA")
        print("===================================")

        print("GERACAO :", geracao, "W")
        print("CONSUMO :", consumo, "W")
        print("DISPONIVEL :", disponivel, "W")

        print("\nSTATUS:")
        print(status)

        print("\nREPRESENTACAO DE DADOS")

        print("Decimal     :", disponivel)

        if disponivel >= 0:
            print("Binario     :", bin(disponivel)[2:])
            print("Hexadecimal :", hex(disponivel)[2:].upper())
        else:
            print("Binario     : valor negativo")
            print("Hexadecimal : valor negativo")

        print("===================================\n")

        sleep(5)