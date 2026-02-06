"""
Selenium WebDriver é uma ferramenta python para o selenium, que permite automatizar a interação com navegadores web.

Para interagir com o navegador é preciso um driver especifico para cada navegador. No caso do Firefox, usamos o GeckoDriver.

"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=service)

url = "https://www.infojobs.com.br/vagas-de-emprego-em-ceara.aspx"

try:
    navegador.get(url)
    
    # 1. LIDANDO COM O POP-UP (Usando Espera Explícita para ser mais rápido)
    try:
        # Espera até 10 segundos para o botão aparecer
        botao_aceitar = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
        )
        botao_aceitar.click()
        print("✅ Termos de uso aceitos.")
    except Exception as e:
        print("⚠️ Botão de termos não apareceu ou já foi fechado.")

    # 2. COLETANDO OS CARDS
    time.sleep(2) # Pequena pausa para garantir que os cards renderizaram
    vagas = navegador.find_elements(By.CLASS_NAME, "js_vacancyLoad")
    
    print(f"--- Analisando {len(vagas)} vagas encontradas ---\n")

    for vaga in vagas:
        try:
            # Dentro do card, procuramos o elemento da data que você achou
            data_elemento = vaga.find_element(By.CLASS_NAME, "text-nowrap")
            data_texto = data_elemento.text.strip()
            
            # 3. FILTRO DE DATA
            if "Hoje" in data_texto:
                # Se for hoje, pegamos o título para confirmar
                titulo = vaga.find_element(By.TAG_NAME, "h2").text
                print(f"📌 NOVA VAGA: {titulo} (Postada: {data_texto})")
            
        except:
            # Algumas vagas no topo podem ser anúncios com estrutura diferente
            continue

finally:
    print("\nBusca finalizada.")
    # Por enquanto, não vamos fechar para você ver o console
    # navegador.quit()