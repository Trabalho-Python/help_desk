from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("ge,_random_uuid()"))
    nome = Column(String, nullable=False, unique=True)
    chamados = relationship("Chamado", back_populates="categoria")