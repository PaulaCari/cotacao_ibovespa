import pyautogui
import webbrowser
import time
import pyperclip
import yfinance
import matplotlib as plt

ticker = input("Digite o codigo da ação desejada: ").upper()

dados = yfinance.Ticker(ticker).history(start="2024-06-04", end="2024-06-05")

fechamento = dados.Close #nome da coluna de fechamento

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_media = round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(valor_media)


destinatario = "produtoscelular@gmail.com"
asunto = "Analisis do projeto 2024"

mensagem = f"""
Prezado Gestor,

Segue a análisis solicitada do projeto da ação periodo de um 18 meses {ticker}:

Cotação máxima: R$ {maxima}
Cotação Minima: R$ {minima}
Cotação Valor medio: R$ {valor_media}

Qualquer duvida entrar em contato, estou a  disposição.

Atte.
MA. Paula
Desenvolvedora em ascensão!!!
pd: enviar codigo de no minimo 5 ações para fazer meus testes
"""

#abrir o navegador
webbrowser.open("www.gmail.com")

# Aguarda 3 segundos para a página carregar
time.sleep(4)

# Configura uma pausa de 6 segundos para permitir que a página seja carregada completamente
pyautogui.PAUSE = 6

# Clica no botão "Escrever"
pyautogui.click(x=105, y=195) # 212

# Cola o email do destinatário no campo "Para" e pressiona TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Cola o assunto no campo "Assunto" e pressiona TAB
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Cola a mensagem no corpo do email 
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clica no botão "Enviar"
pyautogui.click(x=800, y=818)

# Fecha a janela do Gmail
#pyautogui.hotkey("alt", "f4")

# Exibe mensagem de sucesso no terminal
print("Email enviado com sucesso e janela fechada!")


# https://br.financas.yahoo.com/quote/%5EBVSP/history/