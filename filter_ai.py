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


from google import genai


class FiltraVagasAI:
    """Classe para filtrar as vagas usando inteligência artificial."""
    
    def __init__(self, api_key, vagas_hoje, perfil):
        """Incie a classe FiltrarVagasIA.
        
        Atributos:
            _cliente (genai.Client): O cliente da API do GenAI para interagir 
                                    com a inteligência artificial.
            _vagas_hoje (list): Lista de vagas postadas hoje, contendo tuplas 
                                de título e data.
            _perfil (str): O perfil desejado para filtrar as vagas, por exemplo.
        """
        self._cliente = genai.Client(api_key=api_key)
        self._vagas_hoje = vagas_hoje
        self._perfil = perfil
        
    def filtrar_vagas(self):
        """Filtre as vagas usando IA.
        
        Cria um texto bruto com as vagas do dia e um prompt para orientar a IA 
        no processo de filtragem com base no perfil informado.
        """
        texto_bruto = "\n".join([f"{titulo} - Postada ({data})" for titulo, data in self._vagas_hoje])
        
        if not texto_bruto:
            return "Olá boa noite. Passando para te avisar que nenhuma vaga foi encontrada hoje para o perfil especificado."
        
        prompt = f"""
        Você é um recrutador especializado. 
        Analise a lista de vagas abaixo:
        
        {texto_bruto}
        
        Critério de seleção: Vagas estritamente relacionadas a {self._perfil}.
       
        Esqueleto para exemplo de formatação:
        
        Vaga
        Postada em: Hoje
        ---

        Sua tarefa:
        1. Identifique quais vagas combinam com o perfil.
        2. Crie uma mensagem amigável para Telegram, tendo como exemplo o esqueleto informado e formatação Markdown para listagem dessas vagas.
        3. Deixe sempre um espaço em branco para separar as vagas.
        4. Se não houver nenhuma correspondência exata, responda apenas: 
        "Olá boa noite. Passando para te avisar que nenhuma vaga foi encontrada hoje para o perfil especificado."
        """
        
        try:
            resposta = self._cliente.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )
            
            return resposta.text
        except Exception as error:
            print(f"Erro ao filtrar vagas com IA! {error}")