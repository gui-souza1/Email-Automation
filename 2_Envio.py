# PARTE 2: ENVIO AUTOMÁTICO DE E-MAILS

#Importar bibliotecas
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

#Abrir o arquivo CSV <>
arq = pd.read_csv("NomeeEmailClientes.csv")   
    
#configurar seervidor SMTP
servidor_smtp = "smtp.gmail.com"    #servidor SMTP: Gmail
porta = 587                         #porta: Gmail

#configurações de remetente <!>   (conta de quem vai enviar o e-mail)
remetente = "remetente@gmail.com"
senha = "senha_googleapp"

#corpo de texto do e-mail <!>
corpo_texto = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Teste</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
                    <tr>
                        <td align="center" style="padding: 40px 0;">
                            <p style="margin-top: 20px; text-align: center;">Olá,</p>
                            <p style="text-align: center;">paragrafo_1.</p>
                            <p style="text-align: center;">paragrafo_2.</p>
                            <p style="text-align: center;">paragrafo_3.</p>
                            <p style="text-align: center;">paragrafo_4</p>
                            <p style="text-align: center;">paragrafo_5</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
'''

    #Gerando o e-mail 
for linha in arq.index:
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = arq.loc[linha, "E-mail"]
    msg['Subject'] = "Assunto_do_Email" #<!>
    msg.attach(MIMEText(corpo_texto, 'html'))

    #Conectar servidor SMTP
    try:
        servidor = smtplib.SMTP(servidor_smtp, porta)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, arq.loc[linha, "E-mail"], msg.as_string())
        print("E-mail enviado com sucesso.")

    except Exception as e:
        print(f"Houve algum erro {e}")
    finally:
        servidor.quit()
