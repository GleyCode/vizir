"""
Este arquivo ainda está em produção; o fato é que testar automações não é uma 
tarefa fácil, requer tempo, mas temos um caminho, é preciso simular (Mocks) o 
funcionamento do Selenium.
"""

import unittest.mock

from scraper import ColetaInfoVagas


class TestColetaInfoVagas(unittest.TestCase):
    """"""
    def setUP(self):
        """"""
        self.info_jobs = ColetaInfoVagas()
        self.info_jobs._vagas = ["Hoje", "Hoje", "Ontem", "Hoje"]
        
    def test_filtrar_por_data(self):
        """"""
        vagas_hoje = self.info_jobs.filtrar_por_data()
        
        self.assertEqual(vagas_hoje[0][0], "Desenvolvedor Python")
        self.assertEqual(vagas_hoje[0][1], "Hoje")
        
    def test_filtrar_por_data_sem_vagas(self):
        """"""
        vagas_hoje = self.info_jobs.filtrar_por_data()
        self.assertEqual(vagas_hoje, [])
        
"""
class TestFiltraVagasAI(unittest.TestCase):
    """"""
    
    pass


class TestEnvioTelegram(unittest.TestCase):
    """"""
    
    pass
"""

if __name__ == "__main__":
    unittest.main()
