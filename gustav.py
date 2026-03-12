

import pyautogui
import time

# Seu texto com várias linhas
with open('texto.txt', 'r', encoding='utf-8') as f:
    texto = f.read()

# Separa em lista de linhas
linhas = texto.strip().split('/n')

# Abre o WhatsApp Web antes de rodarO term o script
# Deixe o cursor no campo de mensagem!
time.sleep(3)  # tempo para você clicar no campo

for linha in linhas:
    pyautogui.typewrite(linha, interval=0.05)  # digita a linha
    pyautogui.press('enter')                   # envia
    time.sleep(0.05)                              # aguarda entre mensagens