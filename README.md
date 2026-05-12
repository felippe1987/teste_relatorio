# Projeto de Extração e Limpeza de Dados de Relatório

Este projeto estrai e limpa dados de um relatório em PDF para gerar um CSV limpo que pode ser usado para análise e manutenção de dados.

## Estrutura do projeto

- `relatorio.py`
  - Lê o PDF `relatorio.pdf` com `tabula` e concatena todas as tabelas extraídas.
  - Exporta o resultado bruto para `dados_extraidos.csv`.

- `limpeza_dados.py`
  - Lê `dados_extraidos.csv` e aplica limpeza e normalização.
  - Renomeia colunas, remove colunas vazias e formata valores numéricos.
  - Une linhas de continuação de descrição que foram quebradas pelo processo de extração.
  - Converte preços, estoques e códigos para tipos numéricos adequados.
  - Salva o resultado em `dados_limpos.csv`.

- `dados_extraidos.csv`
  - CSV bruto gerado a partir da extração do PDF.

- `dados_limpos.csv`
  - CSV limpo e normalizado, pronto para análise.

## O que foi feito

1. Extração do PDF usando `tabula` para capturar todas as tabelas.
2. Geração de um CSV bruto com os dados extraídos.
3. Criação de um processo de limpeza que:
   - remove colunas geradas incorretamente;
   - trata valores vazios e formatação de texto;
   - padroniza preços e estoque com separador decimal correto;
   - ajusta códigos e referências para inteiros;
   - junta descrições divididas em linhas adicionais.
4. Validação do script de limpeza e geração de `dados_limpos.csv` com sucesso.

## Objetivo

Criar um fluxo reproducível para transformar relatórios em PDF em dados estruturados e prontos para análise em uma planilha excel.

## Como usar

1. Execute a extração do PDF:
   ```bash
   python relatorio.py
   ```
2. Execute a limpeza dos dados:
   ```bash
   python limpeza_dados.py
   ```

## Resultado esperado

- `dados_extraidos.csv` contendo as tabelas extraídas do PDF.
- `dados_limpos.csv` contendo dados tratados, com colunas consistentes e valores numéricos preparados para análise.
