"""FileSystem implementation for the application repository."""

import datetime
import pathlib
from typing import Any, Union

import orjson
from result import Err, Ok, Result
from use_case_registry import UseCaseRegistry

from simple_banking.core.exceptions import UnexpectedError
from simple_banking.core.models import Client
from simple_banking.database.base import IRepository


class FileSystemRepository(IRepository):
    """FileSystem Repository."""

    def __init__(  # noqa: D107
        self,
    ) -> None:
        self.cwd = pathlib.Path().cwd()

        self.path_db = self.cwd / "file_system_db"
        self.path_db.mkdir(parents=True, exist_ok=True)

        self.path_clients = self.path_db / "client.json"
        self.path_clients.touch(exist_ok=True)

    def commit_write_transaction(
        self, write_operations: UseCaseRegistry[str]
    ) -> Result[None, Exception]:
        """Mock commit write transactions."""
        _ = write_operations.get_state()
        write_operations.prune_state()
        return Ok()

    def upsert_client(
        self,
        new_client: Client,
        write_operations: UseCaseRegistry[str],
    ) -> None:
        """Insert client write transaction into the persistance layer."""
        write_operations.add_value(v=f"create client with ID {new_client.client_id}")
        if self.path_clients.read_text() == "":
            clients_as_dict = {}
        else:
            clients_as_dict = orjson.loads(self.path_clients.read_text())
        clients_as_dict[new_client.email] = new_client
        self.path_clients.write_bytes(data=orjson.dumps(clients_as_dict))

        return

    def get_client(self, email: str) -> Result[Union[Client, None], Exception]:
        """Get client from the application file system database."""
        try:
            clients_as_dict: dict[str, Any] = orjson.loads(
                self.path_clients.read_text()
            )
            client_data = clients_as_dict.get(email, None)
            if client_data is None:
                return Ok(None)
            return Ok(
                Client(
                    client_id=client_data["client_id"],
                    email=client_data["email"],
                    name=client_data["name"],
                    last_name=client_data["last_name"],
                    password=client_data["password"],
                    birthday_date=datetime.datetime.strptime(
                        client_data["birthday_date"], "%Y-%m-%d"
                    )
                    .astimezone()
                    .date(),
                )
            )
        except Exception as e:  # noqa: BLE001
            return Err(UnexpectedError(unexpected_error=e))
