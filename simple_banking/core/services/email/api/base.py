"""API interface for Email implementations."""

import abc


class IApiEmail(abc.ABC):
    """Interface defines use cases to be supported by an email service impl."""

    @abc.abstractmethod
    def send_email(
        self,
        to_email: str,
        msg: str,
    ) -> None:
        """Send email to a user."""
