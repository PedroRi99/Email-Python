from email.message import EmailMessage
import ssl
import smtplib

meuEmail = ""
senha = ""
destinatario = ""
assunto = "Testando python"
body = """
Teste
"""
em = EmailMessage()

em['From'] = meuEmail
em['To'] = destinatario
em['subject'] = assunto
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meuEmail, senha)
    smtp.sendmail(meuEmail, destinatario, em.as_string())
