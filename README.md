# Delphi na Gringa — Documentação

Documentação pública do projeto **Delphi na Gringa**, um monitor de oportunidades
para profissionais Delphi no Brasil e no exterior.

> Este repositório contém somente documentação. O código operacional, credenciais,
> banco de dados, logs e configurações privadas não são publicados.

## Objetivo

O projeto organiza alertas de vagas, identifica oportunidades relacionadas a Delphi,
separa vagas nacionais e internacionais e oferece um fluxo de revisão antes da
publicação em redes sociais.

## Fluxo geral

1. Alertas de vagas chegam por e-mail.
2. O coletor extrai título, empresa, localização e link do anúncio.
3. O filtro mantém vagas relacionadas a Delphi e remove duplicatas.
4. As oportunidades são classificadas como Brasil, internacional ou a revisar.
5. O responsável recebe a vaga no painel e no Telegram.
6. A vaga precisa ser verificada antes da aprovação.
7. A arte e a legenda são geradas conforme a classificação.
8. A publicação no Instagram utiliza a API oficial da Meta.

## Funcionalidades documentadas

- Coleta periódica de alertas do Gmail.
- Extração e deduplicação de anúncios.
- Classificação entre Brasil e exterior.
- Aprovação pelo painel e Telegram.
- Controle de vagas encerradas.
- Revalidação e expiração por idade.
- Artes distintas para vagas nacionais e internacionais.
- Preparação para publicação oficial no Instagram.

## Documentação

- [Arquitetura](arquitetura.md)
- [Fluxo de aprovação](fluxo-aprovacao.md)
- [Configuração das integrações](integracoes.md)
- [Segurança e privacidade](seguranca.md)

## Tecnologias

- Python
- FastAPI
- SQLite
- Gmail via IMAP
- Telegram Bot API
- Instagram API
- macOS `launchd`

## Estado

O projeto está em desenvolvimento e utiliza aprovação manual antes de qualquer
publicação. O acesso automatizado não autorizado ao LinkedIn não faz parte do projeto.

## Licença

Documentação disponibilizada sob a licença MIT. Consulte [LICENSE](LICENSE).

