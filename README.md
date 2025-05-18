# Cliente Especialista em Antifraudes com Gemini AI
Projeto relacionado ao conteúdo das aulas 04 e/ou 05 da Imersão IA 2025 Alura com Google Gemini.

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white)](https://ai.google.dev/)


## Visão Geral

Este projeto consiste em um chatbot especialista em antifraudes que utiliza o modelo de linguagem Gemini do Google para analisar se o relato do usuário apresenta indícios de golpe. O conhecimento do especialista é carregado a partir de um arquivo de texto (`.txt`), que contém vários casos famosos de fraudes afim de fornecer contexto ao Gemini durante as consultas.

## Motivações
Dados recentes da Serasa Experian indicam que **metade dos brasileiros (51%) foi vítima de alguma fraude em 2024**, com 54,2% desses sofrendo prejuízo financeiro. Em 2025, o cenário continua preocupante, com o Brasil registrando **mais de 1 milhão de tentativas de fraude pelo segundo mês consecutivo**, o que equivale a uma tentativa a cada 2,2 segundos, conforme também aponta a Serasa Experian.

Esses dados demonstram a urgência de ferramentas que possam educar, informar e auxiliar na prevenção contra essas atividades criminosas.

## Resultados

https://github.com/user-attachments/assets/622eb9b6-a6eb-4fce-92b9-39660d6b52a9


## Instruções para Execução:

1. Gerar e Importar sua chave `GOOGLE_API_KEY` 
2. Instações necessárias:
```!pip install google-genai```
3. Adicionar o arquivo `cartilha-golpe-2025.txt` na pasta `"/content/sample_data"`

## Fontes

A base de dados foi extraida da cartilha Golpe To Fora, Sua reprodução é permitida, desde que citadas as fontes. 
A venda ou comercialização do material é proibida.
Fontes:
- Bárbara Camapum (@podbah.camapum)
- DC Marketing (@tarcisio_dc)
- Operacionais GTTO (@operacionais GTTO e operacionais_gtto)
- Apoio: Delegacia Seccional de Presidente Prudente

**Links para notícias sobre golpes no Brasil:**

* **Metade dos brasileiros sofreu fraude em 2024, diz Serasa Experian:** [https://agenciabrasil.ebc.com.br/economia/noticia/2025-03/metade-dos-brasileiros-sofreu-fraude-em-2024-diz-serasa-experian](https://agenciabrasil.ebc.com.br/economia/noticia/2025-03/metade-dos-brasileiros-sofreu-fraude-em-2024-diz-serasa-experian)
* **Tentativas de golpes aumentam no Brasil - Febraban Tech:** [https://febrabantech.febraban.org.br/temas/seguranca/tentativas-de-golpes-aumentam-no-brasil](https://febrabantech.febraban.org.br/temas/seguranca/tentativas-de-golpes-aumentam-no-brasil)
* **Brasil registra mais de 1 milhão de tentativas de fraude pelo segundo mês consecutivo em 2025, revela Serasa Experian:** [https://www.serasaexperian.com.br/sala-de-imprensa/indicadores/brasil-registra-mais-de-1-milhao-de-tentativas-de-fraude-pelo-segundo-mes-consecutivo-em-2025-revela-serasa-experian/](https://www.serasaexperian.com.br/sala-de-imprensa/indicadores/brasil-registra-mais-de-1-milhao-de-tentativas-de-fraude-pelo-segundo-mes-consecutivo-em-2025-revela-serasa-experian/)
