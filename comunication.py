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


import telebot


class EnvioTelegram:
    """Classe para gerenciar o envio da mensagem pelo Telegram."""
    
    def __init__(self, token, chat_id, relatorio):
        """Inicia o objeto com os seguintes atributos.
        
        Atributos:
            _token: Chave de acesso aAPI do bot Telegram.
            _chat_id: Identificador do bot.
            _relatorio: O texto filtrado pela IA que será enviado ao bot.
            _bot: Conexão com o bot.
        """
        self._token = token
        self._chat_id = chat_id
        self._relatorio = relatorio
        self._bot = telebot.TeleBot(self._token)
        
    def enviar_relatorio(self):
        """Envia a mensagem pelo Telegram.
        
        Envia o texto formatado para Markdown pelo Telegram, utilizado um bot 
        para isso.
        """
        try:
            self._bot.send_message(self._chat_id, self._relatorio, 
                parse_mode='Markdown'
            )
            print("Mensagem enviada ...")
        except Exception as error:
            print(f"Erro ao enviar mensagem: {error}")
