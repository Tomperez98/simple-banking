"""FileSystem implementation for the application repository."""

import pathlib
from typing import Union

import orjson
from result import Ok, Result
from use_case_registry import UseCaseRegistry

from simple_banking.core.models import Client
from simple_banking.database.base import IRepository


class FileSystemRepository(IRepository):
    """FileSystem Repository."""

    def __init__(  # noqa: D107
        self,
    ) -> None:
        self.cwd = pathlib.Path().cwd()
        self.path_clients = self.cwd / "file_system_db" / "clients.json"

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
        prev_client: Union[Client, None],
        new_client: Client,
        write_operations: UseCaseRegistry[str],
    ) -> None:
        """Upsert client write transaction into the persistance layer."""
        if prev_client is None:
            write_operations.add_value(
                v=f"create client with ID {new_client.client_id}"
            )
            clients_as_dict = orjson.loads(self.path_clients.read_text())
            clients_as_dict[new_client.client_id] = new_client
        write_operations.add_value(v=f"update client with ID {new_client.client_id}")
        clients_as_dict = orjson.loads(self.path_clients.read_text())
        clients_as_dict[new_client.client_id] = new_client
        return
