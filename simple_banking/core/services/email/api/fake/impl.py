"""Fake implementation for an email API."""
from simple_banking.core.services.email.api.base import IApiEmail


class FakeApiEmail(IApiEmail):
    """
    Fake Api Email mock functionalities for an email service.

    Useful for unittesting.
    """

    def send_email(self, to_email: str, msg: str) -> None:  # noqa: D102
        _ = to_email
        _ = msg
        return
