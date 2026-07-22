from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.ticket import list_tickets
from app.dependencies import get_db
from app.schemas.ticket import TicketRead


router = APIRouter()


@router.get("/", response_model=list[TicketRead])
def list_tickets_endpoint(db: Session = Depends(get_db)) -> list[TicketRead]:
    return list_tickets(db)
