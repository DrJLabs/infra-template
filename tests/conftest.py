import os

import pytest


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    if os.getenv("DISABLE_MONTFORT") == "1":
        skip_marker = pytest.mark.skip(
            reason="Montfort tests disabled via DISABLE_MONTFORT"
        )
        for item in items:
            if "montfort" in item.keywords:
                item.add_marker(skip_marker)
