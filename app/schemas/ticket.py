import enum
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TicketStatus(str, enum.Enum):
    OPEN = "open"
    STALLED = "stalled"
    CLOSED = "closed"


class TicketBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: str = Field(..., min_length=1)
    status: TicketStatus = TicketStatus.OPEN


class TicketCreate(TicketBase):
    pass


class TicketPut(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: str = Field(..., min_length=1)
    status: TicketStatus = TicketStatus.OPEN


class TicketRead(TicketBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
