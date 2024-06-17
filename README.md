<h1 align="left">PROJETO AUTOMAÇÃO DE EMAILS</h1>

###

<h2 align="left">Introdução</h2>

###

<p align="left">Este projeto consiste na utilização dos dados fornecidos por clientes para automatizar o envio de mensagens de confirmação para seus respectivos e-mails. A intenção foi desenvolver um projeto de aplicação real end-to-end, de forma que toda a operação pudesse ser automatizada. Além disso, o código permite que qualquer pessoa possa utilizá-lo apenas modificando as linhas com informações pessoais (explicadas melhor a seguir**).<br><br>Dessa forma, desde o acesso ao formulário responsável por coletar os dados até a parte final, o envio dos e-mails propriamente dito, todo o processo foi automatizado. No entanto, o código foi dividido em duas etapas : a primeira parte chamada "1_Extração" e a segunda parte chamada "2_Envio".</p>

###

<h3 align="left">Obs:</h3>

###

<p align="left">*Você pode criar um formulário com perguntas próprias ou utilizar o modelo fornecido. Sugiro que a pergunta número 3 continue sendo a mesma (solicitando o endereço de e-mail) para não alterar a posição dessa coluna na planilha de Excel.<br>**É importante saber que <b>as linhas comentadas com a marcação <> são passíveis de modificação</b>, ficando a critério pessoal. No entanto, <b>as linhas com a marcação <!> são de modificação obrigatória</b>.<br>***a automação é iniciada a partir de uma nova guia no google chrome.<br>****como exemplo utilizei somente 4 e-mails, mas poderiam ser mais.</p>

###

<h3 align="left">-> 1_Extração</h3>

###

<p align="left">Consiste na seleção dos dados da planilha de Excel e na extração dos mesmos em arquivo CSV. O link do formulário inserido no código precisa ser o de administrador, não o de solicitação de respostas.</p>

###

<h3 align="left">-> 2_Envio</h3>

###

<p align="left">Após executar a parte 1, será lido o arquivo CSV com a lista de e-mails dos clientes. Antes, é necessário inserir a conta e a senha do Gmail de quem vai enviar o e-mail, bem como o assunto e o texto do e-mail. Após isso, um loop irá percorrer a lista de e-mails e conectar ao servidor SMTP para enviar os e-mails. Uma mensagem aparecerá informando se o e-mail foi enviado ou se houve algum problema.</p>

###

<p align="left">Portanto, basicamente as informações que precisam ser modificadas são:<br>	• Link de administrador do formulário<br>	• Configurações de remetente (login e senha)<br>Assunto e corpo de texto</p>

###



https://github.com/gui-souza1/Email-Automation/assets/162043881/5d47bee0-2c3b-458a-9b57-bcd062d74c8f

