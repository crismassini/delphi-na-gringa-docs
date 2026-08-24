"""Metadados públicos do projeto Delphi na Gringa.

Este arquivo existe para identificar Python como uma das linguagens do repositório
de documentação. Ele não contém código operacional nem credenciais.
"""

PROJECT_NAME = "Delphi na Gringa"
PROJECT_LANGUAGE = "Python"
DOCUMENTATION_ONLY = True


def project_summary() -> str:
    """Retorna uma descrição pública e curta do projeto."""
    return f"{PROJECT_NAME}: documentação pública de um monitor de vagas em {PROJECT_LANGUAGE}."


if __name__ == "__main__":
    print(project_summary())

