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


import os

from scraper import ColetaInfoVagas
from filter_ai import FiltraVagasAI
from comunication import EnvioTelegram


class PipelineVagas:
    """Classe para organizar as instruções de execução do agente."""
    
    def __init__(self):
        """Inicialize a instância com os seguintes atributos.
        
        Atributos:
            _api_key: Chave da API do Geminai.
            _token: Chave de acesso aAPI do bot Telegram.
            _chat_id: Identificador do bot.
            _cidade: Local de publicação das vagas.
            _perfil: Filtra as vagas por um tipo especifico de segmento, por 
                    exemplo, "Logistíca".
        """
        self._api_key = os.getenv("GEMINI_API_KEY")
        self._token = os.getenv("TELEGRAM_TOKEN")
        self._chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self._cidade = "Fortaleza"
        self._perfil = "Qualquer vaga postada."
    
    def executar(self):
        """Execute todas as rotinas do Agente."""
        
        # 1. Coletar e tratrar as vagas do InfoJobs.
        try:
            info_jobs = ColetaInfoVagas()
            info_jobs.configurar_navegador()
            info_jobs.abrir_navegador()
            info_jobs.acessar_pagina()
            info_jobs.aceitar_cookies()
            info_jobs.informar_cidade(self._cidade)
            info_jobs.localizar_vagas()
            vagas_hoje = info_jobs.filtrar_por_data()
        finally:
            info_jobs.fechar_navegador()
    
        # 2. Filtrar as vagas usando IA.
        gen_ai = FiltraVagasAI(self._api_key, vagas_hoje, self._perfil)
        relatorio = gen_ai.filtrar_vagas()
        
        # 3. Enviar a mensagem filtrada para o WhatsApp.
        telegram = EnvioTelegram(self._token, self._chat_id, relatorio)
        telegram.enviar_relatorio()


if __name__ == "__main__":
    """Executa o script para fazer a coleta das vagas."""
    pipeline = PipelineVagas()
    pipeline.executar()