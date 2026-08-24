# Arquitetura

O sistema é dividido em serviços locais independentes:

## Painel administrativo

Interface web local para visualizar vagas, editar informações, verificar validade,
aprovar, descartar e marcar oportunidades como encerradas.

## Coletor de e-mail

Executado periodicamente pelo macOS. Ele acessa o Gmail em modo somente leitura,
extrai anúncios dos alertas e grava somente vagas novas.

## Filtro e classificação

Analisa os campos do anúncio, confirma a relevância para Delphi e classifica a vaga
como nacional, internacional ou não identificada.

## Bot do Telegram

Verifica a fila de notificações, envia as artes para aprovação e registra o resultado
de cada entrega.

## Gerador de arte

Produz imagens verticais em JPEG. Vagas brasileiras usam a identidade vermelha;
oportunidades internacionais usam azul e dourado para maior destaque.

## Instagram

A publicação utiliza a API oficial da Meta, com criação e processamento de container
antes da chamada final de publicação.

