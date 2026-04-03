from bs4 import BeautifulSoup
import requests
import smtplib
import email.message

URL = "https://www.seiziguitars.com.br/produto/baixo-seizi-fun-jazu-jb-4-lava-red-sparkle"

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 OPR/128.0.0.0"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

tittle = soup.find('h1').getText()

price = soup.find('div', class_='product-price').getText()
num_price = price[3:8]
num_price = num_price.replace('.', '')
num_price = float(num_price)

def send_email():
    email_content = """https://www.seiziguitars.com.br/produto/baixo-seizi-fun-jazu-jb-4-lava-red-sparkle"""
    msg = email.message.Message()
    msg.set_payload(email_content)
    msg['Subject'] = "O preço do baixo baixou!!!!!"
    msg['From'] = 'tp.testerprojects@gmail.com'
    msg['To'] = 'tp.testerprojects@gmail.com'
    password = 'otet dbai zopf tein'
    msg.add_header('Content-Type', 'text/html')
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    print("Email enviado com sucesso!")

if (num_price < 5000):
    send_email()




