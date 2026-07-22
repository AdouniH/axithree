from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate


def create_ticket(db: Session, payload: TicketCreate) -> Ticket:
    ticket = Ticket(**payload.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def list_tickets(db: Session) -> list[Ticket]:
    return db.query(Ticket).all()
