"""Client Model."""

import dataclasses
import datetime
import uuid


@dataclasses.dataclass
class Client:
    """Client representation in the application core domain."""

    client_id: uuid.UUID
    email: str
    name: str
    last_name: str
    password: str
    birthday_date: datetime.date
