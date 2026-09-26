from sqlalchemy import Column, Text, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

class HistoricoInteracao(Base):
    __tablename__ = "historico_interacao"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    chamado = Column(UUID(as_uuid=True), ForeignKey("chamados.id", ondelete="CASCADE"), nullable=False)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False)
    descricao = Column(Text, nullable=False)
    data_hora = Column(DateTime(timezone=True), server_default=func.now())

    chamado = relationship("Chamado", back_populates="historico")
