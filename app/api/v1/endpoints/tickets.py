from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud.ticket import create_ticket, list_tickets
from app.dependencies import get_db
from app.schemas.ticket import TicketCreate, TicketRead


router = APIRouter()


@router.post("/", response_model=TicketRead, status_code=status.HTTP_201_CREATED)
def create_ticket_endpoint(payload: TicketCreate, db: Session = Depends(get_db)) -> TicketRead:
    return create_ticket(db, payload)


@router.get("/", response_model=list[TicketRead])
def list_tickets_endpoint(db: Session = Depends(get_db)) -> list[TicketRead]:
    return list_tickets(db)
