# Importa os módulos necessários
import os               # Para interagir com o sistema de arquivos
import json             # Para ler arquivos no formato JSON
import csv              # Para escrever no formato CSV

# Caminho da pasta onde estão os arquivos JSON
pasta_json = "Caminho da pasta"

# Nome de arquivo CSV de saída
arquivo_csv = 'enderecos.csv'

separador = ";"

# Define as colunas que serão usadas no CSV
colunas = ["cep", "logradouro", "complemento", "bairro", "localidade", "uf", "ibge"]

# Abre o arquivo CSV para escrita (modo'w'), com codificação UTF-8
with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    # Cria um objetivo que escreve dicionários no CSV com os nomes das colunas especificadas
    writer = csv.DictWriter(csv_file, fieldnames=colunas, delimiter=separador)

    # Escreve o cabeçalho no arquivo CSV
    writer.writeheader()

    # Itera por todos os arquivos dentro da pasta especificada
    for nome_arquivo in os.listdir(pasta_json):
        # Processa apenas arquivos com extensão .json
        if nome_arquivo.endswith('.json'):
            # Monta o caminho completo do arquivo
            caminho_aquivio = os.path.join(pasta_json, nome_arquivo)
            try:
                # Abre o arquivo JSON
                with open(caminho_aquivio, 'r', encoding='utf-8') as f:
                    # Carrega os dados do JSON em um dicionário
                    dados = json.load(f)

                    # Cria uma linha do CSV com dados das colunas, usando '' como valor padrão se a chave não existir
                    linha = {coluna: dados.get(coluna, '') for coluna in colunas}

                    # Escreve a linha do arquivo CSV
                    writer.writerow(linha)
            except Exception as e:
                # Em caso de erro, exibe uma mensagem indicando qual o arquivo causou o problema
                print(f"Erro ao processar '{nome_arquivo}': {e}")

# Mensagem final indicando sucesso na criação do CSV                
print(f'\n CSV "{arquivo_csv}" criado com sucesso com todos os arquivos de {pasta_json}')