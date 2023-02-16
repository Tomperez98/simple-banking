"""Configuration for the persistance layer."""

import inject

from simple_banking.database import FileSystemRepository
from simple_banking.database.base import IRepository


def dependency_injection(binder: inject.Binder) -> None:
    """Configure dependency injection for the persistance layer."""
    binder.bind(
        cls=IRepository,
        instance=FileSystemRepository(),
    )
