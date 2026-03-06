"""
Vizir
Copyright (C) 2026 Abraão Silva

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ColetaInfoVagas:
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
        self._url = "https://www.infojobs.com.br/"
        self._navegador = None
        self._service = None
        self._vagas = []
        self._options = None

    def configurar_navegador(self):
        """Configure o Firefox.
        
        Configura as opções do Firefox, ativando a opção --headless para rodar 
        sem interface gráfica.
        """
        try:            
            self._options = FirefoxOptions() # Modo headless
            #self._options.add_argument("--headless")
        except Exception as error:
            print(f"Erro ao configurar o navegador: {error}")
    
    def abrir_navegador(self):
        """Abra o navegador em modo headless.
        
        Iniciar o navegador em modo headless Firefox usando o serviço 
        configurado.
        """
        try:
            self._navegador = webdriver.Firefox(options=self._options)
        except Exception as error:
            print(f"Erro ao abrir o navegador: {error}")
        
    def fechar_navegador(self):
        """Encerre o navegador.
        
        Verfica se a sessão do navegador está ativa e a encerra.
        """
        if self._navegador:
            self._navegador.quit()
    
    def acessar_pagina(self):
        """Acesse o conteúdo da página.
        
        Acessa a URL especificada no atributo `_url` e baixa o HTML, CSS, JS, 
        imagens, etc.
        """
        try:
            self._navegador.get(self._url)
        except Exception as error:
            print(f"Possivelmente encontrado um erro com a URL informada: {error}")
            
    def aceitar_cookies(self):
        """Clique no botão de aceitar termos.
        
        Usa uma espera explícita para aguardar o botão de aceitar termos 
        aparecer e clicar nele. Se o botão não aparecer dentro do tempo limite, 
        lança uma exceção.
        """
        try:
            aceitar_cookies = WebDriverWait(self._navegador, 10).until(
                EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
            )
            aceitar_cookies.click()
        except Exception as error:
            print(f"Botão não encontrado. {error}")
    
    def informar_cidade(self, cidade):
        """Vá para a página de vagas disponível para a cidade informada.
        
        Acessa o elemento de busca do InfoJobs, digita o nome de uma cidade,
        selecina a primeira opção na lista de sugestões e finaliza simulando o 
        pressionamento da tecla ENTER.
        """
        try:
            informar_cidade = WebDriverWait(self._navegador, 5).until(
                EC.element_to_be_clickable((By.ID, "city"))
            )
            informar_cidade.clear()
            informar_cidade.send_keys(cidade)
            time.sleep(2) # Aguarda as sugestões aparecer.
            informar_cidade.send_keys(Keys.ARROW_DOWN) # Seleciona a primeira sugestão.
            informar_cidade.send_keys(Keys.ENTER)
        except Exception as error:
            print(f"Campo não encontrado. {error}")
    
    # TODO: Alterar a classe que identifica os cards, o correto é: "card"
    def localizar_vagas(self):
        """Encontre os cards de vagas.
        
        Aguarda 2 segundos para garantir que os cards foram carregados e, em 
        seguida, encontra todos os elementos com a classe "js_vacancyLoad", que 
        representam os cards de vagas.
        """
        try:
            time.sleep(2)
            self._vagas = self._navegador.find_elements(By.CLASS_NAME, 
                        "js_rowCard"
                        )
        except Exception as error:
            print(f"Erro encontrado ao buscar as classes HTML: {error}")
        
    def filtrar_por_data(self):
        """Filtre as vagas por data.
        
        Filtra as vagas postadas "Hoje" e imprime o título e o texto de postado 
        "Hoje".
        """
        vagas_hoje = []
        for vaga in self._vagas:
            try:
                data_elemento = vaga.find_element(By.CLASS_NAME, "text-nowrap")
                data_texto = data_elemento.text.strip()
                
                if "Hoje" in data_texto:  # aqui devo coletar todas as informações. 
                    titulo = vaga.find_element(By.TAG_NAME, "h2").text
                    """
                    funcao = vaga.find_element(By.CLASS_NAME, "h3").text
                    cidade = vaga.find_element(By.CLASS_NAME, "mb-8").text
                    salario = vaga.find_element(By.)
                    requisitos = ""
                    modalidade = ""
                    descricao = ""
                    """
                    vagas_hoje.append((titulo, data_texto))
            except:
                continue
        return vagas_hoje