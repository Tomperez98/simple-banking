"""Email service configuration."""
import inject

from simple_banking.core.services.email.api.base import IApiEmail
from simple_banking.core.services.email.api.fake import FakeApiEmail


def dependency_injection(binder: inject.Binder) -> None:
    """Configure dependency injection for the Email service."""
    binder.bind(
        cls=IApiEmail,
        instance=FakeApiEmail(),
    )
