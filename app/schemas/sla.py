import uuid
from datetime import datetime
from pydantic import BaseModel

class SLAResponse(BaseModel):
    chamado_id: uuid.UUID
    prioridade: str
    prazo_sla: datetime
    sla_vencido: bool