"""Custom Exceptions."""


class UnexpectedError(Exception):
    """Error raised when something unexpected went wrong."""

    def __init__(self, unexpected_error: Exception) -> None:
        """Construct error."""
        super().__init__(f"Something unexpected went wrong {unexpected_error}")
