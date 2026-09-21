# Sprint 3 – Controle Inteligente de Sessão de Recarga

## Integrantes

- Aneliza Rondina - RM-572977
- Arthur Costa - RM-569976
- Guilherme Detta - RM-569666
- Henrique Bolfer - RM-569514
- Igor Alves - RM-574127
- Rafaella Ferreira - RM-571030

---

## Objetivo

Desenvolver um protótipo funcional utilizando Raspberry Pi Pico e MicroPython para simular um sistema inteligente de controle de sessão de recarga baseado na disponibilidade de energia.

---

## Funcionamento

O sistema recebe dois valores:

- Geração de energia
- Consumo da residência

Realizando o cálculo:

Energia Disponível = Geração - Consumo

Com base no resultado são definidos três estados:

### 🟢 Recarga Autorizada

Energia suficiente para realizar a recarga.

### 🟡 Recarga Reduzida

Energia disponível limitada.

### 🔴 Recarga Bloqueada

Energia insuficiente para realizar a recarga.

---

## Cenários Demonstrados

### Situação 1

Geração: 4000 W

Consumo: 1500 W

Disponível: 2500 W

Resultado: RECARGA AUTORIZADA

---

### Situação 2

Geração: 1800 W

Consumo: 1500 W

Disponível: 300 W

Resultado: RECARGA REDUZIDA

---

### Situação 3

Geração: 1000 W

Consumo: 1800 W

Disponível: -800 W

Resultado: RECARGA BLOQUEADA

---

## Arquitetura de Computadores

### Entrada

Dados simulados de:

- Geração de energia
- Consumo da residência

### Processamento

O Raspberry Pi Pico realiza o cálculo:

Energia Disponível = Geração - Consumo

e determina o estado da sessão de recarga.

### Memória

Os dados são armazenados nas variáveis:

- geracao
- consumo
- disponivel
- status

### Saída

O sistema apresenta os resultados através:

- LEDs
- Monitor Serial

---

## Representação de Dados

Exemplo utilizando o valor 2500:

Decimal: 2500

Binário: 100111000100

Hexadecimal: 9C4

---

## Tecnologias Utilizadas

- Raspberry Pi Pico
- MicroPython
- Wokwi
