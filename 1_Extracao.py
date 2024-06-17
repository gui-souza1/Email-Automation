# PARTE 1: EXTRAIR DADOS DOS CLIENTES (EXCEL -> CSV)

#importar bibliotecas
import pyautogui
import time

#função para otimizar time.sleep()
delay = 2
def click_delay(x, y):
    pyautogui.click(x=x, y=y)
    time.sleep(delay)

pyautogui.PAUSE = 0.5

#MAIN : acessar os dados (Excel online)
time.sleep(delay)
pyautogui.click(x=238, y=65)
pyautogui.write("https://forms.office.com/") #<!> Endereço do link do formulario (microsoft forms; como adm)
time.sleep(2)
pyautogui.press('enter')  
time.sleep(delay)
click_delay(178, 163)
click_delay(923, 383)
time.sleep(15)
#Processo coluna1 (nomes)
click_delay(816,475)      
click_delay(823,305)
pyautogui.hotkey('ctrl', 'c')
click_delay(174, 690)           
pyautogui.hotkey('ctrl', 'v')
click_delay(131, 684)
#Processo coluna2 (E-mails)
click_delay(1103, 477)      
click_delay(1093, 274 )
pyautogui.hotkey('ctrl', 'c')
click_delay(201, 688)
click_delay(142, 303)
pyautogui.hotkey('ctrl', 'v')
#Alterar nome das colunas
click_delay(77, 285)         # coluna nome
pyautogui.write("Nome")  
pyautogui.press('enter')
click_delay(140, 285)         # coluna e-mail
pyautogui.write("E-mail")  
pyautogui.press('enter')
#Exportar CSV
click_delay(43, 148)          
click_delay(82, 480)
click_delay(340, 237)
pyautogui.write("NomeeEmailClientes.csv")  # <> nome do arquivo csv
pyautogui.press('enter')


