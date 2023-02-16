"""InMemory implemenation for the application repository."""
from typing import Union

from result import Ok, Result
from use_case_registry import UseCaseRegistry

from simple_banking.core.models import Client
from simple_banking.database.base import IRepository


class InMemoryRepository(IRepository):
    """
    InMemory Repository mocks the persistance layer.

    Useful for unittesting.
    """

    def __init__(  # noqa: D107
        self,
    ) -> None:
        self.clients: dict[str, Client] = {}

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
        """Mock upsert client write transaction into the persistance layer."""
        if prev_client is None:
            write_operations.add_value(
                v=f"create client with ID {new_client.client_id}"
            )
            self.clients[new_client.email] = new_client
            return
        write_operations.add_value(v=f"update client with ID {new_client.client_id}")
        self.clients[new_client.email] = new_client
        return
