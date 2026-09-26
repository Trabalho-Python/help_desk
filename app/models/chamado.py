from sqlalchemy import Column, String, Text, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

status_chamado = ENUM(
    "aberto", "em_andamento", "resolvido", "fechado",
    name = "status_chamado",
    create_type = False
)

prioridade_chamado = ENUM(
    "baixa", "media", "alta",
    name = "prioridade_chamado",
    create_type = False
)

class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    status = Column(status_chamado, nullable=False, server_default="aberto")
    prioridade = Column(prioridade_chamado, nullable=False)
    prazo_sla = Column(DateTime(timezone=True), nullable=True)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False)
    categoria_id = Column(UUID(as_uuid=True), ForeignKey("categorias.id", ondelete="RESTRICT"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    usuario = relationship("Usuario", back_populates="chamados")
    categoria = relationship("Categoria", back_populates="chamados")
    historico = relationship("HistoricoInteracao", back_populates="chamado")
