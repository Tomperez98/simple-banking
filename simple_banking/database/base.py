"""Application Repository Interface."""

import abc
from typing import Any, Union

from result import Result
from use_case_registry import UseCaseRegistry

from simple_banking.core.models import Client


class IRepository(abc.ABC):
    """Application repository interface decouples the persistency from core domain."""

    @abc.abstractmethod
    def commit_write_transaction(
        self, write_operations: UseCaseRegistry[Any]
    ) -> Result[None, Exception]:
        """Commit a set of write operations as a transaction."""

    @abc.abstractmethod
    def upsert_client(
        self,
        prev_client: Union[Client, None],
        new_client: Client,
        write_operations: UseCaseRegistry[Any],
    ) -> None:
        """Insert/Upsert client in the application persistance layer."""

    @abc.abstractmethod
    def get_client(self, email: str) -> Result[Union[Client, None], Exception]:
        """Get a client from the application database."""
