import pytest

from infrastructure.clients.montfort import MontfortClient


@pytest.mark.montfort
def test_montfort_fetch_data() -> None:
    client = MontfortClient()
    data = client.fetch_data()
    assert data
