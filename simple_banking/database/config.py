"""Configuration for the persistance layer."""

import inject

from simple_banking.database.base import IRepository
from simple_banking.database.in_memory import InMemoryRepository


def dependency_injection(binder: inject.Binder) -> None:
    """Configure dependency injection for the persistance layer."""
    binder.bind(
        cls=IRepository,
        instance=InMemoryRepository(),
    )
