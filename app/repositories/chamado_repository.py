import uuid

from sqlalchemy.orm import Session

from app.models.chamado import Chamado
from app.services.sla_calculator import calcular_prazo_sla


def buscar_chamado_por_id(db: Session, chamado_id: uuid.UUID) -> Chamado | None:
    return db.query(Chamado).filter(Chamado.id == chamado_id).first()


def calcular_e_salvar_sla(db: Session, chamado_id: uuid.UUID) -> Chamado | None:
    chamado = buscar_chamado_por_id(db, chamado_id)

    if chamado is None:
        return None

    chamado.prazo_sla = calcular_prazo_sla(chamado.prioridade, chamado.created_at)

    db.commit()
    db.refresh(chamado)

    return chamado