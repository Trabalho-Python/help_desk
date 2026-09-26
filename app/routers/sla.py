import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.chamado_repository import calcular_e_salvar_sla
from app.schemas.sla import SLAResponse
from app.services.sla_status import sla_esta_vencido

router = APIRouter(prefix="/sla", tags=["SLA"])


@router.post("/calcular/{chamado_id}", response_model=SLAResponse)
def calcular_sla(chamado_id: uuid.UUID, db: Session = Depends(get_db)):
    chamado = calcular_e_salvar_sla(db, chamado_id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")

    return SLAResponse(
        chamado_id=chamado.id,
        prioridade=chamado.prioridade,
        prazo_sla=chamado.prazo_sla,
        sla_vencido=sla_esta_vencido(chamado.prazo_sla),
    )