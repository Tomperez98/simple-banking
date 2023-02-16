"""Email client."""


from typing import cast

import inject
from result import Err, Ok, Result

from simple_banking.core.exceptions import UnexpectedError
from simple_banking.core.services.email.api.base import IApiEmail


class EmailClient:
    """Email client exposes use cases supported by an Email service."""

    def __init__(self) -> None:
        """Entry point for the email service."""
        self.api = cast(IApiEmail, inject.instance(cls=IApiEmail))

    def send_email(self, to_email: str, msg: str) -> Result[None, Exception]:
        """Send an email."""
        try:
            self.api.send_email(to_email=to_email, msg=msg)
            return Ok()
        except Exception as e:  # noqa: BLE001
            return Err(UnexpectedError(unexpected_error=e))
