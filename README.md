# Conver-o-de-JSON-para-CSV
## Descrição
Script Python para conversão de múltiplos arquivos JSON em um único arquivo CSV consolidado. Processa todos os arquivos '.json' de um diretório, extrai campos específicos e gera um CSV unifica do com codificação UTF-8. Ideal para organização de dados estruturados de APIs ou sistemas.

## Funcionalidades
* **Processamento em Lote**: Converte todos os arquivos JSON de uma pasta automaticamente.
* **Seleção de Campos**: Extrai apenas campos específicos definidos (CEP, logradouro, bairro, etc.)
* **Tratamento de Erros**: Identifica arquivos problemáticos sem interromper o processamento.
* **Codificação UTF-8**: Suporte a caracteres especiais e acentuação.
* **Delimitador Customizável**: Configuração do separador de campos do CSV (padrão: ';').

## Como Usar
#### 1. **Configuração**:
* Altere a variável 'pasta_json' no script para o caminho da sua pasta com arquivos JSON.
* Opcional: Modifique a lista 'colunas' para os campos desejados ou o 'separador' se necessário.
#### 2. **Execução**:
```bash
python conversão.py
```
#### 3. **Saída**:
* Arquivo enderecos.csv gerado na mesma pasta do script.
* Erros são exibidos no console durante o processamento.

## Estrutura do JSON
Os arquivos JSON devem conter pelo menos um dos seguintes campos (exemplo):
```bash
{
    "cep": "01001-00",
    "logradouro": "Praça da Sé",
    "complemento": "lado ímpar",
    "bairro": "Sé",
    "localidade": "São Paulo",
    "uf": "SP",
    "ibge": "3550308"
}
```
## Dependências
- Python 3.6+
- Bibliotecas Padrão:
    - `os` para manipulação de 
    - `json` para leitura de arquivos JSON
    - `csv` para escrita do arquivo CSV

## Instalação
Nenhuma instalação adicional necessária - apenas execute o script:
```bash
git clone https://github.com/seu-usuario/JSON-to-CSV-Converter.git
cd JSON-to-CSV-Converter
python json_to_csv.py
```
## Exemplo de Uso
#### Entrada (pasta com JSONs):
```bash
/enderecos
  ├── endereco1.json
  ├── endereco2.json
  └── endereco3.json
```
#### Saída:
```bash
cep;logradouro;complemento;bairro;localidade;uf;ibge
01001-000;Praça da Sé;lado ímpar;Sé;São Paulo;SP;3550308
20010-020;Avenida Rio Branco;;Centro;Rio de Janeiro;RJ;3304557
```
## Notas 
* Campos não encontrados nos JSONs serão preenchidos com string vazia
* Arquivos JSON mal formatados serão ignorados e reportados no console
* Para usar vírgula como separador, altere `separador = ","`
* Compatível com Windows/Linux/MacOS