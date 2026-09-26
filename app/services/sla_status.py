from datetime import datetime, timezone

def sla_esta_vencido(prazo_sla: datetime) -> bool:
    agora = datetime.now(timezone.utc)
    return agora > prazo_sla