from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ColetarInfoVagas:
    """Classe para coletar informações de vagas de emprego no site InfoJobs 
    usando Selenium WebDriver.
    """
    
    def __init__(self):
        """Inicie a classe ColetarInfoVagas.
        
        Define a URL alvo e inicializa os atributos necessários.
        
        Atributos:
            _url (str): A URL da página de vagas de emprego no InfoJobs.
            _navegador (WebDriver): O objeto WebDriver do Selenium.
            _service (Service): O serviço do GeckoDriver (Firefox).
            _vagas (list): Lista de elementos WebDriver representando as vagas.
            """
        self._url = "https://www.infojobs.com.br/vagas-de-emprego-em-ceara.aspx"
        self._navegador = None
        self._service = None
        self._vagas = None

    def configurar_navegador(self):
        """Configure o Firefox.
        
        Configura de forma automática o Firefox usando o GeckoDriverManager.
        """
        self._service = Service(GeckoDriverManager().install())
    
    def abrir_navegador(self):
        """Abra o navegador.
        
        Iniciar o navegador Firefox usando o serviço configurado.
        """
        self._navegador = webdriver.Firefox(service=self._service)
        
    def fechar_navegador(self):
        """Encerre o navegador.
        
        Verfica se a sessão do navegador está ativa e a encerra.
        """
        if self._navegador:
            self._navegador.quit()
    
    def baixar_pagina(self):
        """Baixe o conteúdo da página.
        
        Acessa a URL especificada no atributo `_url` e baixa o HTML, CSS, JS, 
        imagens, etc.
        """
        self._navegador.get(self._url)
        
    def aceitar_cookies(self):
        """Clique no botão de aceitar termos.
        
        Usa uma espera explícita para aguardar o botão de aceitar termos 
        aparecer e clicar nele. Se o botão não aparecer dentro do tempo limite, 
        lança uma exceção.
        """
        try:
            botao_aceitar = WebDriverWait(self._navegador, 10).until(
                EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
            )
            botao_aceitar.click()
        except Exception as error:
            raise Exception(f"Botão não encontrado. {error}")
    
    def localizar_vagas(self):
        """Encontre os cards de vagas.
        
        Aguarda 2 segundos para garantir que os cards foram carregados e, em 
        seguida, encontra todos os elementos com a classe "js_vacancyLoad", que 
        representam os cards de vagas.
        """
        time.sleep(2)
        self._vagas = self._navegador.find_elements(By.CLASS_NAME, "js_vacancyLoad")
        
    def filtrar_por_data(self):
        """Filtre as vagas por data.
        
        Filtra as vagas postadas "Hoje" e imprime o título e o texto de postado 
        "Hoje".
        """
        for vaga in self._vagas:
            try:
                data_elemento = vaga.find_element(By.CLASS_NAME, "text-nowrap")
                data_texto = data_elemento.text.strip()
                
                if "Hoje" in data_texto:
                    titulo = vaga.find_element(By.TAG_NAME, "h2").text
                    print(f"NOVA VAGA: {titulo} (Postada: {data_texto})")
            except Exception as error:
                continue
            

if __name__ == "__main__":
    """Executa o script para fazer a coleta das vagas."""
    info_jobs = ColetarInfoVagas()
    info_jobs.configurar_navegador()
    info_jobs.abrir_navegador()
    info_jobs.baixar_pagina()
    info_jobs.aceitar_cookies()
    info_jobs.localizar_vagas()
    info_jobs.filtrar_por_data()
    info_jobs.fechar_navegador()