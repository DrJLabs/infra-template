import os
from typing import Protocol


class MontfortProtocol(Protocol):
    """Minimal interface for the Montfort client."""

    def fetch_data(self) -> str:
        """Return data from the service."""


class StubMontfortClient:
    """Stub implementation used when Montfort access is disabled."""

    def fetch_data(self) -> str:
        return "stub"


class RealMontfortClient:
    """Real implementation performing HTTP requests."""

    def fetch_data(self) -> str:
        import requests  # type: ignore

        response = requests.get("https://example.com")
        response.raise_for_status()
        return response.text


MontfortClient = (
    StubMontfortClient if os.getenv("DISABLE_MONTFORT") == "1" else RealMontfortClient
)


__all__ = ["MontfortClient", "MontfortProtocol"]
