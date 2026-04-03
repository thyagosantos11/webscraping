# Web Scraper - Monitor de Preço

## Técnica utilizada

Web scraping com **BeautifulSoup** + **Requests**. O script simula um header de navegador para evitar bloqueios, localiza elementos HTML por tags e classes específicas, extrai texto bruto, limpa e converte dados (ex: preço de string para float) e aplica lógica condicional para disparar alertas via e-mail (SMTP Gmail).

## Funcionamento

1. Requisição HTTP com header personalizado
2. Parsing do HTML com BeautifulSoup
3. Extração de título (`<h1>`) e preço (`div.product-price`)
4. Tratamento do preço (remoção de pontos e conversão para float)
5. Comparação com valor alvo (R$ 5.000)
6. Disparo automático de e-mail se condição for atendida

## Tecnologias

- Python 3
- BeautifulSoup4
- Requests
- smtplib

## ⚠️ Atenção

As credenciais de e-mail estão expostas no código. Para uso real, utilize variáveis de ambiente.
