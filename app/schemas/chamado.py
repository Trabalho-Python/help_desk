import uuid
from datetime import datetime 
from typing import Optional

from pydantic import BaseModel

class ChamadoOut(BaseModel):
    id: uuid.UUID
    titulo: str
    descricao: str
    status: str
    prioridade: str
    prazo_sla: Optional[datetime] = None
    usuario_id: uuid.UUID
    categoria_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True