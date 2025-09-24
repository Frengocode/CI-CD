import pytest
import aiohttp
from typing import Any
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_get_hello() -> None:
    async with aiohttp.ClientSession() as client:
        response = await client.get("http://app:8000/hello/")
        assert response.status == 200

        data: dict[str, Any] = await response.json()
        log.info("Test finished successfully ! %s ", data)
        assert data.get("detail") == "Hello world !"
