# TelegramCovidBot

Chatbot de consulta dos dados relacionados à COVID-19 no telegram. Utiliza o Watson Assistant como gerenciador e a "API Dataset covid19 no Brasil.IO" para consultas.
- Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e equipe de voluntários Brasil.IO
- Brasil.IO: boletins epidemiológicos da COVID-19 por município por dia, disponível em: https://brasil.io/dataset/covid19/

## Branches

O projeto tem apenas a branch master

## Configurações

Para execução do chatbot basta acessar o telegram e consultar por "@DadosCovidChatBot" ou utilizar o link https://web.telegram.org/#/im?p=%40DadosCovidChatBot

## Funcionalidades disponíveis

* O chatbot possui 4 consultas ao todo:
    - 2 para dados totais de COVID-19 - consulta por um Estado específico, no qual retorna os dados consolidados do Estado e de cada cidade desse Estado. E consulta de todos os Estados, somente com os dados consolidados dos Estados brasileiros.
    - 2 para os novos casos de COVID-19 ocorridos nas últimas 24hs - consulta por um Estado específico, no qual retorna os dados consolidados do Estado e de cada cidade desse Estado. E consulta de todos os Estados, somente com os dados consolidados dos Estados brasileiros.