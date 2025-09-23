import pytest
import aiohttp
from typing import Any


@pytest.mark.asyncio
async def test_get_hello() -> None:
    async with aiohttp.ClientSession() as client:
        response = await client.get("http://localhost:8000/hello/")
        assert response.status == 200

        data: dict[str, Any] = await response.json()
        assert data.get("detail") == "Hello world !"
