
def main(vagas_hoje):
    texto_bruto = ""
    for vaga in vagas_hoje:
        for info in range(len(vaga)):
            texto_bruto += vaga[info] + "\n"
        texto_bruto += "\n"
    return texto_bruto
                
if __name__ == "__main__":
    vagas_hoje = [
        ("Desenvolvedor Python", "Hoje", "Desenvolvimento de software", "São Paulo", "R$ 5.000,00", "Empresa A"),
        ("Analista de Dados", "Hoje", "Análise de dados", "Rio de Janeiro", "R$ 4.000,00", "Empresa B"),
        ("Gerente de Projetos", "Hoje", "Gerenciamento de projetos", "Belo Horizonte", "R$ 6.000,00", "Empresa C")
    ]
    print(main(vagas_hoje))