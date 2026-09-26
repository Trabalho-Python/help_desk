from sqlalchemy import inspect

from app.core.database import engine
from app.models import usuario, categoria, chamado, historico_interacao  # noqa: F401


def testar_conexao():
    try:
        inspector = inspect(engine)
        tabelas = inspector.get_table_names()
        print("Conexão bem-sucedida! Tabelas encontradas no banco:")
        for tabela in tabelas:
            print(f"  - {tabela}")
    except Exception as erro:
        print("Erro ao conectar no banco:")
        print(erro)


if __name__ == "__main__":
    testar_conexao()